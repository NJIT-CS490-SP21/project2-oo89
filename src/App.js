import React, { useState, useRef, useEffect } from "react";
import { calculateWinner } from "./helper";
import Board from "./Board";
import io from 'socket.io-client';

const socket = io(); // Connects to socket connection

const App = () => {
  const [history, setHistory] = useState([Array(9).fill(null)]);
  const [stepNumber, setStepNumber] = useState(0);
  const [xIsNext, setXisNext] = useState(true);
  const winner = calculateWinner(history[stepNumber]);
  const xO = xIsNext ? "X" : "O";
  
  //User 
  const [activeUsers, setUsers] = useState([]);
  const [username, setusername] = useState(null);  
  const usernameRef = useRef(null); // This is the reference to the input element  username 
  const [xOLogin, setxOLogin] = useState('X'); 
  // hiding the board 
  const [isShown, setShown] = useState(false); 
  
  function loginClick () {
     const userText = usernameRef.current.value; 
     setUsers(prevUsers => {
       const listUserCopy = [...prevUsers]; 
       listUserCopy.push(userText); 
       
       return listUserCopy; 
     });
     
    //this is to show ot not the board when login  
    setShown((prevShown) => {
      return !prevShown;
    });
    
    
   socket.emit('login', {userText:userText,xOLogin:xOLogin }); 
   

  }
  
  useEffect(() => {
      socket.on('login', (data) => {
      console.log('Login event received!');
      console.log(data);
      setUsers(prevUser => [...prevUser, data.userText]);
      setxOLogin('O');
    });
      
    }, []);
  
  const sqClick = (i) => {
    
    
    const historyPoint = history.slice(0, stepNumber + 1);
    const current = historyPoint[stepNumber];
    const squares = [...current];
    
    // return if won or occupied
    if (winner || squares[i]) {
      return;
    } 
    // select square
    squares[i] = xO;
    setHistory([...historyPoint, squares]);
    setStepNumber(historyPoint.length);
    setXisNext(!xIsNext);
    
    //socket.emit('eventData',{squares: squares});
    socket.emit('eventData',{squares:squares});
    
    
    //socket.emit('eventData2', setXisNext)
    console.log(current);
    console.log(squares);
  };
  
  const jumpTo = (step) => {
    setStepNumber(step);
    setXisNext(step % 2 === 0);
    
  };

  useEffect(() => {
    // Listening for a chat event emitted by the server. If received, we
    // run the code in the function that is passed in as the second arg
      socket.on('eventData', (data) => {
        console.log('Square received!');
        console.log(data);
      // If the server sends a message (on behalf of another client), then we
      // add it to the list of messages to render it on the UI.
      //  setHistory(current => [...current, data.squares]);
      setHistory(current => [...current, data.squares]);
      
    });
    
  }, []);

  const renderMoves = () =>
    history.map((_step, move) => {
      const destination = move ? `Go to move #${move}` : "Start";
      return (
        <li key={move}>
          <button onClick={() => jumpTo(move)}>{destination}</button>
        </li>
      );
    });

  return (
    <>
      <h1>Tic Tac Toe - Oscar Project2 CS490</h1>
      <div>
      
      {isShown === false ? (
        <div>
      <input ref={usernameRef} type="text" /> 
        <button onClick={() => loginClick()}> Login </button>
       
      </div>
      ):null}
      
         <div>
        {activeUsers.map((item, index) => (
          <li>{item} {index===0 ? "X" : index===1 ? "O" : "spectator"} </li> //if index ==0 print x else if index==1 print o else spec
        ))}
       </div>
       
       {isShown === true ? ( 
           <div>
      <Board squares={history[stepNumber]} onClick={sqClick} />
      
      <div className="info-wrapper">
        <div>
          <h3>History</h3>
          {renderMoves()}
        </div>
        <h3>{winner ? "Winner: " + winner : "Next Player: " + xO}</h3>
      </div>
      </div>
         ): null }
      </div>
      
    
    </>
    
  );
};

export default App;