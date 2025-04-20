// src/api/auth.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // Adjust if different

export const loginUser = async (email, password) => {
  const response = await axios.post(`${API_URL}/token/`, {
    email,
    password,
  });

  const { access, refresh } = response.data;

  // Save tokens
  localStorage.setItem('accessToken', access);
  localStorage.setItem('refreshToken', refresh);

  return response.data;
};

export const logoutUser = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
};
