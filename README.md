# E-commerce Sales Chatbot

A modern, interactive sales chatbot for e-commerce platforms that enhances customer experience through intelligent product search and purchase assistance.

## Recent Changes and Updates

### New Environment Variables
Add these to your `.env` file:
```
REACT_APP_API_URL=http://localhost:5000    # Base URL for API calls
REACT_APP_WS_URL=ws://localhost:5000/ws    # WebSocket URL for real-time chat
```

### New Features Added
1. **Real-time Chat System**
   - WebSocket integration for instant messaging
   - Message history persistence
   - Auto-scrolling chat window
   - User/support message differentiation

2. **Product Management**
   - Redux state management for products
   - Cart functionality
   - Product search with API integration
   - Loading states and error handling

3. **Order Management**
   - Order history with expandable details
   - Status tracking with color indicators
   - API integration for order data
   - Date formatting and display

### API Integration
- Replaced mock data with actual API calls
- Added proper error handling
- Implemented loading states
- Added authentication token management

## Features

- 🤖 Interactive chatbot interface for product search and assistance
- 🔐 Secure user authentication and session management
- 📱 Responsive design for desktop, tablet, and mobile devices
- 🔍 Advanced product search and filtering capabilities
- 💾 Persistent chat history and session tracking
- 🛍️ Mock e-commerce inventory with 100+ products
- 🔄 Real-time product updates and availability

## Tech Stack

### Frontend
- React.js
- Material-UI for responsive design
- Redux for state management
- Axios for API communication
- React Router for navigation

### Backend
- Python 3.8+
- Flask framework
- SQLAlchemy ORM
- PostgreSQL database
- JWT for authentication
- Flask-CORS for cross-origin support

## Project Structure

```
e-commerce-chatbot/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   ├── store/          # Redux store
│   │   └── utils/          # Utility functions
│   └── public/             # Static files
│
├── backend/                 # Flask backend application
│   ├── app/
│   │   ├── models/         # Database models
│   │   ├── routes/         # API routes
│   │   ├── services/       # Business logic
│   │   └── utils/          # Utility functions
│   ├── tests/              # Unit tests
│   └── config.py           # Configuration
│
└── docs/                   # Documentation
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- PostgreSQL
- npm or yarn

### Backend Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   flask db upgrade
   flask seed-db  # Populates mock data
   ```

4. Run the backend server:
   ```bash
   flask run
   ```

### Frontend Setup
1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
   ```

## API Documentation

The API documentation is available at `/api/docs` when running the backend server.

### Key Endpoints
- `POST /api/auth/login` - User authentication
- `GET /api/products` - List products
- `POST /api/chat` - Chatbot interaction
- `GET /api/orders` - User orders

## Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Challenges and Solutions

### Challenge 1: Real-time Chat Updates
**Solution**: Implemented WebSocket connections for real-time chat updates while maintaining RESTful API for other operations.

### Challenge 2: Product Search Accuracy
**Solution**: Implemented fuzzy search with multiple criteria and category-based filtering to improve search accuracy.

### Challenge 3: Session Management
**Solution**: Used JWT tokens with refresh mechanism and Redis for session storage to maintain secure and persistent sessions.

## Future Improvements

1. Integration with payment gateways
2. Advanced analytics dashboard
3. Multi-language support
4. Voice-based interactions
5. AI-powered product recommendations 

## Demo video [unable to upload the video]
