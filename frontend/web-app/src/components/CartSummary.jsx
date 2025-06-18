import React from 'react';

const CartSummary = ({ totalItems, onSubmitOrder }) => {
  if (totalItems === 0) return null;

  return (
    <div className="cart-summary">
      <p>Выбрано товаров: {totalItems}</p>
      <button onClick={onSubmitOrder}>Купить</button>
    </div>
  );
};

export default CartSummary;