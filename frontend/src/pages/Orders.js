import React, { useState } from 'react';
import {
  Container,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
  Chip,
  Box,
  IconButton,
  Collapse,
} from '@mui/material';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';

// Mock data - replace with actual API call
const mockOrders = [
  {
    id: 'ORD001',
    date: '2024-03-15',
    total: 299.99,
    status: 'Delivered',
    items: [
      { name: 'Product 1', quantity: 2, price: 149.99 },
      { name: 'Product 2', quantity: 1, price: 99.99 },
    ],
  },
  {
    id: 'ORD002',
    date: '2024-03-14',
    total: 199.99,
    status: 'Processing',
    items: [
      { name: 'Product 3', quantity: 1, price: 199.99 },
    ],
  },
];

const OrderRow = ({ order }) => {
  const [open, setOpen] = useState(false);

  const getStatusColor = (status) => {
    switch (status.toLowerCase()) {
      case 'delivered':
        return 'success';
      case 'processing':
        return 'warning';
      case 'cancelled':
        return 'error';
      default:
        return 'default';
    }
  };

  return (
    <>
      <TableRow sx={{ '& > *': { borderBottom: 'unset' } }}>
        <TableCell>
          <IconButton size="small" onClick={() => setOpen(!open)}>
            {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
          </IconButton>
        </TableCell>
        <TableCell>{order.id}</TableCell>
        <TableCell>{order.date}</TableCell>
        <TableCell>${order.total.toFixed(2)}</TableCell>
        <TableCell>
          <Chip
            label={order.status}
            color={getStatusColor(order.status)}
            size="small"
          />
        </TableCell>
      </TableRow>
      <TableRow>
        <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={5}>
          <Collapse in={open} timeout="auto" unmountOnExit>
            <Box sx={{ margin: 2 }}>
              <Typography variant="h6" gutterBottom component="div">
                Order Details
              </Typography>
              <Table size="small">
                <TableHead>
                  <TableRow>
                    <TableCell>Product</TableCell>
                    <TableCell align="right">Quantity</TableCell>
                    <TableCell align="right">Price</TableCell>
                    <TableCell align="right">Total</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {order.items.map((item, index) => (
                    <TableRow key={index}>
                      <TableCell>{item.name}</TableCell>
                      <TableCell align="right">{item.quantity}</TableCell>
                      <TableCell align="right">${item.price.toFixed(2)}</TableCell>
                      <TableCell align="right">
                        ${(item.quantity * item.price).toFixed(2)}
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Box>
          </Collapse>
        </TableCell>
      </TableRow>
    </>
  );
};

const Orders = () => {
  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h4" gutterBottom>
        Order History
      </Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell />
              <TableCell>Order ID</TableCell>
              <TableCell>Date</TableCell>
              <TableCell>Total</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {mockOrders.map((order) => (
              <OrderRow key={order.id} order={order} />
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
};

export default Orders; 