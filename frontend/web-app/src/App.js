import React, { useEffect, useState } from 'react';
import { getProducts, sendOrder } from './api/api';
import ProductCard from './components/ProductCard';
import CartSummary from './components/CartSummary';
import './styles/App.css';
window.Telegram.WebApp.expand();
function App() {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState({});
  const [userData, setUserData] = useState(null);

  // Загрузка данных при запуске
  useEffect(() => {
    if (window.Telegram && window.Telegram.WebApp) {
      const webApp = window.Telegram.WebApp;
      webApp.ready();

      const user = webApp.initDataUnsafe?.user;
      if (user) {
        setUserData({
          telegram_id: user.id,
          first_name: user.first_name,
          last_name: user.last_name || '',
        });
      }
    }

    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      const data = await getProducts();
      setProducts(data);
    } catch (err) {
      console.error('Ошибка загрузки товаров:', err);
    }
  };

  const handleQuantityChange = (productId, delta) => {
    setCart(prev => {
      const currentQty = prev[productId] || 0;
      const newQty = Math.max(0, currentQty + delta);
      if (newQty === 0) {
        const copy = { ...prev };
        delete copy[productId];
        return copy;
      }
      return { ...prev, [productId]: newQty };
    });
  };

  const handleSubmitOrder = async () => {


  const { telegram_id } = { telegram_id: 898836844 };
  // Формируем массив заказов по каждому товару
  const orders = products
    .filter(p => cart[p.id])
    .map(p => ({
      user_id: telegram_id,
      product_id: p.id,
      quantity: cart[p.id],
    }));

  try {
    await sendOrder(orders); // отправляем массив заказов
    alert('Извените! Нет Товаров на Складе');
    setCart({});
  } catch (err) {
    alert('Ошибка при отправке заказа.');
    console.error(err);
  }
};

  const totalItems = Object.values(cart).reduce((sum, qty) => sum + qty, 0);

return (
  <div className="app">
    <div className="shop-header">
      <h1 className="shop-title">PLA Shop</h1>
    </div>

    <div className="products-grid">
      {products.map(product => (
        <ProductCard
          key={product.id}
          product={{
            ...product,
            quantity: cart[product.id] || 0
          }}
          onIncrease={() => handleQuantityChange(product.id, 1)}
          onDecrease={() => handleQuantityChange(product.id, -1)}
        />
      ))}
    </div>

    <CartSummary
      totalItems={totalItems}
      onSubmitOrder={handleSubmitOrder}
    />
  </div>
);
}

export default App;