import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  user: null,
  isAuthenticated: false,
  accessToken: null,
  refreshToken: null,
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    login: (state, action) => {
      const { user, access_token, refresh_token } = action.payload;
      state.user = user;
      state.isAuthenticated = true;
      state.accessToken = access_token;
      state.refreshToken = refresh_token;
      
      // Store tokens in localStorage
      localStorage.setItem('accessToken', access_token);
      localStorage.setItem('refreshToken', refresh_token);
    },
    logout: (state) => {
      state.user = null;
      state.isAuthenticated = false;
      state.accessToken = null;
      state.refreshToken = null;
      
      // Clear tokens from localStorage
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
    },
    updateTokens: (state, action) => {
      const { access_token } = action.payload;
      state.accessToken = access_token;
      localStorage.setItem('accessToken', access_token);
    },
  },
});

export const { login, logout, updateTokens } = authSlice.actions;
export default authSlice.reducer; 