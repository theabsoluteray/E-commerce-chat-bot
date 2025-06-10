import React, { useState } from 'react';
import {
  Container,
  Grid,
  Card,
  CardContent,
  CardMedia,
  Typography,
  Button,
  Box,
  Rating,
  TextField,
  InputAdornment,
} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';

// Mock data - replace with actual API call
const mockProducts = [
  {
    id: 1,
    name: 'Premium Headphones',
    price: 199.99,
    rating: 4.5,
    image: 'https://via.placeholder.com/300x200',
    description: 'High-quality wireless headphones with noise cancellation.',
  },
  {
    id: 2,
    name: 'Smart Watch',
    price: 299.99,
    rating: 4.2,
    image: 'https://via.placeholder.com/300x200',
    description: 'Feature-rich smartwatch with health monitoring.',
  },
  {
    id: 3,
    name: 'Wireless Earbuds',
    price: 149.99,
    rating: 4.7,
    image: 'https://via.placeholder.com/300x200',
    description: 'True wireless earbuds with premium sound quality.',
  },
  {
    id: 4,
    name: 'Bluetooth Speaker',
    price: 89.99,
    rating: 4.3,
    image: 'https://via.placeholder.com/300x200',
    description: 'Portable Bluetooth speaker with 360° sound.',
  },
];

const Products = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [cart, setCart] = useState([]);

  const handleAddToCart = (product) => {
    setCart([...cart, product]);
    // Here you would typically update the cart state in your global state management
    // and possibly make an API call to update the backend
  };

  const filteredProducts = mockProducts.filter((product) =>
    product.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Box sx={{ mb: 4 }}>
        <Typography variant="h4" gutterBottom>
          Products
        </Typography>
        <TextField
          fullWidth
          variant="outlined"
          placeholder="Search products..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchIcon />
              </InputAdornment>
            ),
          }}
        />
      </Box>

      <Grid container spacing={3}>
        {filteredProducts.map((product) => (
          <Grid item key={product.id} xs={12} sm={6} md={4} lg={3}>
            <Card
              sx={{
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                '&:hover': {
                  transform: 'translateY(-4px)',
                  transition: 'transform 0.2s ease-in-out',
                },
              }}
            >
              <CardMedia
                component="img"
                height="200"
                image={product.image}
                alt={product.name}
              />
              <CardContent sx={{ flexGrow: 1 }}>
                <Typography gutterBottom variant="h6" component="h2">
                  {product.name}
                </Typography>
                <Typography
                  variant="body2"
                  color="text.secondary"
                  sx={{ mb: 2 }}
                >
                  {product.description}
                </Typography>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <Rating value={product.rating} precision={0.5} readOnly />
                  <Typography variant="body2" sx={{ ml: 1 }}>
                    ({product.rating})
                  </Typography>
                </Box>
                <Typography variant="h6" color="primary" sx={{ mb: 2 }}>
                  ${product.price.toFixed(2)}
                </Typography>
                <Button
                  variant="contained"
                  fullWidth
                  startIcon={<ShoppingCartIcon />}
                  onClick={() => handleAddToCart(product)}
                >
                  Add to Cart
                </Button>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default Products; 