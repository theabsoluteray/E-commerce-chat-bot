import React, { useState, useEffect, useRef } from 'react';
import { Box, TextField, Button, Paper, Typography, Container } from '@mui/material';
import SendIcon from '@mui/icons-material/Send';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (newMessage.trim()) {
      setMessages([...messages, {
        text: newMessage,
        sender: 'user',
        timestamp: new Date().toLocaleTimeString()
      }]);
      setNewMessage('');
      // Here you would typically make an API call to your backend
      // and handle the response
    }
  };

  return (
    <Container maxWidth="md" sx={{ height: 'calc(100vh - 100px)', py: 4 }}>
      <Paper elevation={3} sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
        <Box sx={{ p: 2, bgcolor: 'primary.main', color: 'white' }}>
          <Typography variant="h6">Customer Support Chat</Typography>
        </Box>
        
        <Box sx={{ 
          flex: 1, 
          overflow: 'auto', 
          p: 2,
          display: 'flex',
          flexDirection: 'column',
          gap: 2
        }}>
          {messages.map((message, index) => (
            <Box
              key={index}
              sx={{
                alignSelf: message.sender === 'user' ? 'flex-end' : 'flex-start',
                maxWidth: '70%',
              }}
            >
              <Paper
                elevation={1}
                sx={{
                  p: 2,
                  bgcolor: message.sender === 'user' ? 'primary.light' : 'grey.100',
                  color: message.sender === 'user' ? 'white' : 'text.primary',
                }}
              >
                <Typography variant="body1">{message.text}</Typography>
                <Typography variant="caption" sx={{ display: 'block', mt: 1 }}>
                  {message.timestamp}
                </Typography>
              </Paper>
            </Box>
          ))}
          <div ref={messagesEndRef} />
        </Box>

        <Box
          component="form"
          onSubmit={handleSendMessage}
          sx={{
            p: 2,
            bgcolor: 'background.paper',
            borderTop: 1,
            borderColor: 'divider',
            display: 'flex',
            gap: 1,
          }}
        >
          <TextField
            fullWidth
            variant="outlined"
            placeholder="Type your message..."
            value={newMessage}
            onChange={(e) => setNewMessage(e.target.value)}
            size="small"
          />
          <Button
            type="submit"
            variant="contained"
            endIcon={<SendIcon />}
            disabled={!newMessage.trim()}
          >
            Send
          </Button>
        </Box>
      </Paper>
    </Container>
  );
};

export default Chat; 