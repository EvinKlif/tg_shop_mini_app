import React from 'react';

const ProductCard = ({ product, onIncrease, onDecrease }) => {
  const quantity = product.quantity || 0;

  return (
    <div className="product-card">
      {/* Фото */}
      <img
        src={`$'http://backend:8000'/media/${product.photo_url}`}
        alt={product.name}
        className="product-image"
      />

      {/* Название */}
      <h6>{product.name}</h6>

      {/* Цена */}
      <p>Цена: {product.price} ₽</p>

      {/* Счетчик */}
      <div className="quantity-controls">
        <button
          onClick={onDecrease}
          className="quantity-btn minus"
          disabled={quantity <= 0}
        >
          −
        </button>
        <span className="quantity-display">{quantity}</span>
        <button onClick={onIncrease} className="quantity-btn plus">
          +
        </button>
      </div>
    </div>
  );
};

export default ProductCard;