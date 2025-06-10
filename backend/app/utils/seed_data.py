from app import db
from app.models.product import Product
import random

def seed_products():
    """Seed the database with mock product data."""
    categories = [
        'Electronics',
        'Books',
        'Clothing',
        'Home & Kitchen',
        'Sports & Outdoors'
    ]
    
    electronics = [
        {
            'name': 'Laptop Pro X1',
            'description': 'High-performance laptop with 16GB RAM and 512GB SSD',
            'price': 1299.99,
            'stock': 50,
            'category': 'Electronics',
            'image_url': 'https://example.com/laptop.jpg'
        },
        {
            'name': 'Smartphone Y2',
            'description': 'Latest smartphone with 128GB storage and 5G capability',
            'price': 899.99,
            'stock': 100,
            'category': 'Electronics',
            'image_url': 'https://example.com/phone.jpg'
        },
        {
            'name': 'Wireless Earbuds',
            'description': 'Noise-cancelling wireless earbuds with 24-hour battery life',
            'price': 199.99,
            'stock': 200,
            'category': 'Electronics',
            'image_url': 'https://example.com/earbuds.jpg'
        }
    ]
    
    books = [
        {
            'name': 'Python Programming',
            'description': 'Comprehensive guide to Python programming language',
            'price': 49.99,
            'stock': 150,
            'category': 'Books',
            'image_url': 'https://example.com/python-book.jpg'
        },
        {
            'name': 'Web Development Basics',
            'description': 'Learn HTML, CSS, and JavaScript fundamentals',
            'price': 39.99,
            'stock': 100,
            'category': 'Books',
            'image_url': 'https://example.com/web-dev.jpg'
        }
    ]
    
    clothing = [
        {
            'name': 'Men\'s T-Shirt',
            'description': 'Comfortable cotton t-shirt available in multiple colors',
            'price': 24.99,
            'stock': 300,
            'category': 'Clothing',
            'image_url': 'https://example.com/tshirt.jpg'
        },
        {
            'name': 'Women\'s Jeans',
            'description': 'Classic fit denim jeans with stretch comfort',
            'price': 59.99,
            'stock': 200,
            'category': 'Clothing',
            'image_url': 'https://example.com/jeans.jpg'
        }
    ]
    
    home_kitchen = [
        {
            'name': 'Coffee Maker',
            'description': 'Programmable coffee maker with thermal carafe',
            'price': 79.99,
            'stock': 75,
            'category': 'Home & Kitchen',
            'image_url': 'https://example.com/coffee-maker.jpg'
        },
        {
            'name': 'Blender Pro',
            'description': 'High-speed blender for smoothies and food processing',
            'price': 129.99,
            'stock': 50,
            'category': 'Home & Kitchen',
            'image_url': 'https://example.com/blender.jpg'
        }
    ]
    
    sports = [
        {
            'name': 'Yoga Mat',
            'description': 'Non-slip yoga mat with carrying strap',
            'price': 29.99,
            'stock': 150,
            'category': 'Sports & Outdoors',
            'image_url': 'https://example.com/yoga-mat.jpg'
        },
        {
            'name': 'Running Shoes',
            'description': 'Lightweight running shoes with cushioned sole',
            'price': 89.99,
            'stock': 100,
            'category': 'Sports & Outdoors',
            'image_url': 'https://example.com/running-shoes.jpg'
        }
    ]
    
    all_products = electronics + books + clothing + home_kitchen + sports
    
    # Add products to database
    for product_data in all_products:
        product = Product(**product_data)
        db.session.add(product)
    
    try:
        db.session.commit()
        print(f"Successfully seeded {len(all_products)} products")
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding products: {str(e)}")

if __name__ == '__main__':
    seed_products() 