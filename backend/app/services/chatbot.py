import re
from app.models.product import Product

class ChatbotService:
    def __init__(self):
        self.commands = {
            'search': self._handle_search,
            'help': self._handle_help,
            'categories': self._handle_categories,
            'price': self._handle_price
        }
    
    def process_message(self, message):
        """Process user message and generate appropriate response."""
        message = message.lower().strip()
        
        # Check for commands
        for command, handler in self.commands.items():
            if message.startswith(command):
                return handler(message)
        
        # Default response for unrecognized commands
        return self._handle_help(message)
    
    def _handle_search(self, message):
        """Handle product search requests."""
        # Extract search query
        query = message.replace('search', '').strip()
        if not query:
            return "Please provide a search term. For example: 'search laptop'"
        
        # Search products
        products = Product.search(query)
        
        if not products:
            return f"I couldn't find any products matching '{query}'. Try a different search term or browse categories."
        
        # Format response
        response = f"I found {len(products)} products matching '{query}':\n\n"
        for product in products[:5]:  # Show top 5 results
            response += f"- {product.name} (${product.price:.2f})\n"
        
        if len(products) > 5:
            response += f"\n... and {len(products) - 5} more products."
        
        return response
    
    def _handle_help(self, message):
        """Provide help information."""
        return """I can help you with the following commands:
- search [term]: Search for products
- categories: Show available product categories
- price [min] [max]: Search products within price range
- help: Show this help message

For example, try 'search laptop' or 'categories'."""
    
    def _handle_categories(self, message):
        """Show available product categories."""
        categories = db.session.query(Product.category).distinct().all()
        categories = [cat[0] for cat in categories if cat[0]]
        
        if not categories:
            return "No categories available at the moment."
        
        response = "Available categories:\n\n"
        for category in categories:
            response += f"- {category}\n"
        
        return response
    
    def _handle_price(self, message):
        """Handle price range search."""
        # Extract price range
        try:
            prices = re.findall(r'\d+', message)
            if len(prices) != 2:
                return "Please specify both minimum and maximum prices. For example: 'price 100 500'"
            
            min_price, max_price = map(float, prices)
            products = Product.search(min_price=min_price, max_price=max_price)
            
            if not products:
                return f"No products found between ${min_price} and ${max_price}."
            
            response = f"Found {len(products)} products between ${min_price} and ${max_price}:\n\n"
            for product in products[:5]:
                response += f"- {product.name} (${product.price:.2f})\n"
            
            if len(products) > 5:
                response += f"\n... and {len(products) - 5} more products."
            
            return response
            
        except ValueError:
            return "Please provide valid price numbers. For example: 'price 100 500'" 