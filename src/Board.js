import React, { useEffect } from 'react';
// import io from 'socket.io-client';
import Square from './Square';

const Board = ({ squares, onClick }) => {
  useEffect(() => {
    console.log('component Board did mount');
  }, []);

  return (
    <div className="board">
      {squares.map((square, i) => (
        <Square key={i} value={square} onClick={() => onClick(i)} />
      ))}
    </div>
  );
};
export default Board;
