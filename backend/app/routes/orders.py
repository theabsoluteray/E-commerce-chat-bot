from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.order import Order, OrderItem
from app.models.product import Product

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['GET'])
@jwt_required()
def get_orders():
    user_id = get_jwt_identity()
    orders = Order.query.filter_by(user_id=user_id).order_by(Order.created_at.desc()).all()
    
    return jsonify({
        'orders': [order.to_dict() for order in orders]
    }), 200

@orders_bp.route('/<int:order_id>', methods=['GET'])
@jwt_required()
def get_order(order_id):
    user_id = get_jwt_identity()
    order = Order.query.filter_by(id=order_id, user_id=user_id).first_or_404()
    
    return jsonify(order.to_dict()), 200

@orders_bp.route('/', methods=['POST'])
@jwt_required()
def create_order():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['items', 'shipping_address']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Validate items
    if not isinstance(data['items'], list) or not data['items']:
        return jsonify({'error': 'Order must contain at least one item'}), 400
    
    # Calculate total amount and validate products
    total_amount = 0
    order_items = []
    
    for item in data['items']:
        if not all(k in item for k in ['product_id', 'quantity']):
            return jsonify({'error': 'Each item must have product_id and quantity'}), 400
        
        product = Product.query.get(item['product_id'])
        if not product:
            return jsonify({'error': f'Product {item["product_id"]} not found'}), 404
        
        if product.stock < item['quantity']:
            return jsonify({'error': f'Insufficient stock for product {product.name}'}), 400
        
        total_amount += product.price * item['quantity']
        order_items.append({
            'product': product,
            'quantity': item['quantity'],
            'price': product.price
        })
    
    # Create order
    order = Order(
        user_id=user_id,
        total_amount=total_amount,
        shipping_address=data['shipping_address']
    )
    db.session.add(order)
    db.session.flush()  # Get order ID
    
    # Create order items and update stock
    for item in order_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product'].id,
            quantity=item['quantity'],
            price_at_time=item['price']
        )
        db.session.add(order_item)
        
        # Update product stock
        item['product'].stock -= item['quantity']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Order created successfully',
        'order': order.to_dict()
    }), 201

@orders_bp.route('/<int:order_id>/cancel', methods=['POST'])
@jwt_required()
def cancel_order(order_id):
    user_id = get_jwt_identity()
    order = Order.query.filter_by(id=order_id, user_id=user_id).first_or_404()
    
    if order.status != 'pending':
        return jsonify({'error': 'Only pending orders can be cancelled'}), 400
    
    # Restore product stock
    for item in order.items:
        product = Product.query.get(item.product_id)
        product.stock += item.quantity
    
    order.status = 'cancelled'
    db.session.commit()
    
    return jsonify({
        'message': 'Order cancelled successfully',
        'order': order.to_dict()
    }), 200 