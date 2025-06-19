import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

const api = axios.create({
  baseURL: API_URL,
});

export const getProducts = async () => {
  try {
    const res = await api.get('/api/products/');
    return res.data.map(product => ({
      ...product,
      photo_url_full: `${API_URL}/media/${product.photo_url}`,
    }));
  } catch (err) {
    console.error('Ошибка получения товаров:', err);
    return [];
  }
};

export const sendOrder = async (orders) => {
  const res = await api.post('/api/orders/', orders);
  return res.data;
};