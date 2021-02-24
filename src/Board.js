import React, {useEffect} from "react";
import Square from "./Square";
import io from 'socket.io-client';



const Board = ({ squares, onClick })  =>{
  
    useEffect(() => {
    console.log("component Board did mount");
  },[]);
  
  
  
  return(
  
  <div className="board">
    {squares.map((square, i) => (
      <Square key={i} value={square} onClick={() => onClick(i)} />
    ))}
  </div>
  );
};
export default Board;