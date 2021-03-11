import React, { useEffect } from 'react';
// import io from "socket.io-client";

const Square = ({ value, onClick }) => {
  const style = value ? `squares ${value}` : 'squares';

  useEffect(() => {
    console.log('component Square did mount');
  }, []);

  return (
    <button type="button" className={style} onClick={onClick}>
      {value}
    </button>
  );
};

export default Square;
