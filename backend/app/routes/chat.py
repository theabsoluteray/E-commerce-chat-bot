from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.chat import ChatSession, ChatMessage
from app.models.product import Product
from app.services.chatbot import ChatbotService

chat_bp = Blueprint('chat', __name__)
chatbot_service = ChatbotService()

@chat_bp.route('/sessions', methods=['GET'])
@jwt_required()
def get_sessions():
    user_id = get_jwt_identity()
    sessions = ChatSession.query.filter_by(user_id=user_id).order_by(ChatSession.created_at.desc()).all()
    
    return jsonify({
        'sessions': [session.to_dict() for session in sessions]
    }), 200

@chat_bp.route('/sessions', methods=['POST'])
@jwt_required()
def create_session():
    user_id = get_jwt_identity()
    
    # Create new chat session
    session = ChatSession(user_id=user_id)
    db.session.add(session)
    db.session.commit()
    
    # Add welcome message
    welcome_message = ChatMessage(
        session_id=session.id,
        content="Hello! I'm your shopping assistant. How can I help you today?",
        sender='bot'
    )
    db.session.add(welcome_message)
    db.session.commit()
    
    return jsonify(session.to_dict()), 201

@chat_bp.route('/sessions/<int:session_id>/messages', methods=['GET'])
@jwt_required()
def get_messages(session_id):
    user_id = get_jwt_identity()
    session = ChatSession.query.filter_by(id=session_id, user_id=user_id).first_or_404()
    
    return jsonify({
        'messages': [message.to_dict() for message in session.messages]
    }), 200

@chat_bp.route('/sessions/<int:session_id>/messages', methods=['POST'])
@jwt_required()
def send_message(session_id):
    user_id = get_jwt_identity()
    session = ChatSession.query.filter_by(id=session_id, user_id=user_id).first_or_404()
    
    data = request.get_json()
    if not data or 'content' not in data:
        return jsonify({'error': 'Message content is required'}), 400
    
    # Save user message
    user_message = ChatMessage(
        session_id=session.id,
        content=data['content'],
        sender='user'
    )
    db.session.add(user_message)
    
    # Process message and generate bot response
    bot_response = chatbot_service.process_message(data['content'])
    
    # Save bot response
    bot_message = ChatMessage(
        session_id=session.id,
        content=bot_response,
        sender='bot'
    )
    db.session.add(bot_message)
    db.session.commit()
    
    return jsonify({
        'user_message': user_message.to_dict(),
        'bot_message': bot_message.to_dict()
    }), 200

@chat_bp.route('/sessions/<int:session_id>', methods=['DELETE'])
@jwt_required()
def delete_session(session_id):
    user_id = get_jwt_identity()
    session = ChatSession.query.filter_by(id=session_id, user_id=user_id).first_or_404()
    
    # Delete all messages in the session
    ChatMessage.query.filter_by(session_id=session.id).delete()
    
    # Delete the session
    db.session.delete(session)
    db.session.commit()
    
    return jsonify({
        'message': 'Chat session deleted successfully'
    }), 200 