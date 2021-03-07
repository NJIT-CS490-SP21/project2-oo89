import React, { useState, useRef, useEffect } from "react";
import { calculateWinner } from "./helper";
import Board from "./Board";
import io from 'socket.io-client';
import { ListItem } from './ListItem.js';

const socket = io(); // Connects to socket connection

const App = () => {
  //board history and all the other useState I'll need 
  const [history, setHistory] = useState([Array(9).fill(null)]);
  
  const [stepNumber, setStepNumber] = useState(0);
  const [xIsNext, setXisNext] = useState(true);
  const winner = calculateWinner(history[stepNumber]);
  const xO = xIsNext ? "X" : "O";
  
  //User and all the vars I need in the login 
  const [activeUsers, setUsers] = useState([]);
  const [username, setusername] = useState(null);  
  const usernameRef = useRef(null); // This is the reference to the input element  username 
  
  // hiding the board 
  const [isShown, setShown] = useState(false); 
  // Hiding the leaderboard 
  const [isShownLB, setShownLB] = useState(false); 
  
  //DB users and scores 
  const [dbUserList, setdbUserList] = useState([]);
  const [dbScoreList, setdbScoreList] = useState([]);
  
  
  // Function onclick for login information 
  function loginClick () {
     const userText = usernameRef.current.value;
     if(userText ===""){
       alert("User Name is required");
       return;
     }
     setUsers(prevUsers => {
       const listUserCopy = [...prevUsers]; 
       listUserCopy.push(userText); 
       
       return listUserCopy; 
     });
     
    //this is to show ot not the board when login  
    setShown((prevShown) => {
      return !prevShown;
    });
  
   socket.emit('login', {userText:userText}); 
   
  }
  //useEffect for login information 
  useEffect(() => {
      socket.on('login', (data) => {
      console.log('Login event received!');
      console.log(data);
      setUsers(prevUser => [...prevUser, data.userText]);
      
    });

    }, []);
    
    useEffect(() => {
     //I have to emit all the change o the db to here
      socket.on('user_dic', (data)=> {
      console.log('User Dic event received!');
      console.log(data);
      
      setdbUserList(data.users)
      setdbScoreList(data.scores)
      });
      
    }, []);
  //This is the onclick function on each square 
  const sqClick = (i) => {
    
    
    const historyPoint = history.slice(0, stepNumber + 1);
    const current = historyPoint[stepNumber];
    const squares = [...current];
    
    // return if won or occupied
    if (winner || squares[i]) {
      console.log("Winner" + winner);
      return;
    } 
 
    // select square
    squares[i] = xO;
    setHistory([...historyPoint, squares]);
    setStepNumber(historyPoint.length);
    setXisNext(!xIsNext);
    
    //Emit what I need to the sever. 
    socket.emit('eventData',{squares:squares, i:i, history:history, stepNumber:stepNumber, xIsNext:xIsNext, xO:xO });
    
    //some console log to see what I needed. 
    console.log(i);
    console.log(squares);
    console.log(history);
    
  };
//For board 
  useEffect(() => {
    // Listening for a chat event emitted by the server. If received, we
    // run the code in the function that is passed in as the second arg
      socket.on('eventData', (data) => {
        console.log('Square received!');
        console.log(data);
      // If the server sends a message (on behalf of another client), then we
      // add it to the list of messages to render it on the UI.
      const historyPointCopy = (data.history).slice(0, data.stepNumber + 1);
      const currentCopy = historyPointCopy[data.stepNumber];
      const squaresCopy = [...currentCopy];
      
      
      if (winner || squaresCopy[data.i]) 
      {
        return;
      } 
      squaresCopy[data.i] = data.xO;
      setHistory([...historyPointCopy, squaresCopy]);
      setStepNumber(historyPointCopy.length);
      setXisNext(!(data.xIsNext));
      console.log(history);
      console.log(historyPointCopy);
      //  setHistory(current => [...current, data.squares]);
      //setHistory(current => [...current, data.squares]);
      
    });
    
  }, []);

//onClick to hide or show leaderboard 
  function leaderboardSHClick () {
    setShownLB((prevShownLB) => {
      return !prevShownLB;
    }); 
  }
  
  //jump to is used in the history and to restart the game 
  const jumpTo = (step) => {
    
    setStepNumber(step);
    setXisNext(step % 2 === 0);
    socket.emit('jump',{stepNumber:stepNumber,xIsNext:xIsNext, step:step});
  };
  
  useEffect(() => {
     //I have to emit all the change o the db to here
      socket.on('jump', (data)=> {
      console.log('Jump received!');
      console.log(data);
      const setStepNumberCopy = data.step;
      
      setStepNumber(setStepNumberCopy);
      setXisNext(data.step % 2 ===0);
      });
      
    }, []);
  
  //For Winner 
  useEffect(() => {
      var winnerName = "";
      var loserName = "";
      console.log("Winner--" + winner);
      if(winner === "X")
      {
          winnerName = activeUsers[0];
          if(activeUsers.length>1)
          {
            console.log("The Winner I want "+ winnerName)
            loserName = activeUsers[1];
            console.log("The loser I want "+loserName)
            socket.emit('winnerN', {'winner':winnerName, 'loser':loserName});
          }
          else
          {
            alert("One player doesn’t count to the score\nPlease refresh the game or click on Restar\nMake sure you click 'ok' in all of the windows you have open\n");
          }
          
      }
      else if(winner === "O")
      {
          
          if(activeUsers.length>1)
          {
            winnerName = activeUsers[1];
            loserName = activeUsers[0];
            socket.emit('winnerN', {'winner':winnerName, 'loser':loserName});
          }
          else
          {
            alert("One player doesn’t count to the score\nPlease refresh the game or click on Restar\nMake sure you click 'ok' in all of the windows you have open\n");
          }
          

      }
    
    }, [winner]);
    
  // Renders Move  
  const renderMoves = () =>
    history.map((_step, move) => {
      const destination = move ? `Go to move #${move}` : "Restart";
      return (
        <li key={move}>
          <button onClick={() => jumpTo(move)}>{destination}</button>
        </li>
      );
    });
    
  const renderTable = dbUserList.map((value, index) => {
    const linkContent = dbScoreList[index];
    return (
     
      <tr>      
        <td>{value}</td>
        <td>{linkContent}</td>
      </tr>

    
    );
  });
     

  return (
    <>
      <h1>Tic Tac Toe - Oscar Project2 CS490</h1>
      <div>
      
      {isShown === false ? (
      <div className="loginD">
        <label for="uname"><b>Username</b></label>
        <input ref={usernameRef} type="text" placeholder="Enter Username" required/> 
        <button className="loginButton" onClick={() => loginClick()}> Login </button>
        
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
          <button onClick={() => leaderboardSHClick()}> show/Hide Leaderboard</button>
          <button>Enjoy the Game</button>
          <button>{winner ? "Winner: " + winner : "Next Player: " + xO}</button>
          <h3>Steps in history</h3>
          {renderMoves()}
        </div>
      </div>
      
      {isShownLB === true ? (
      
        <div className="score-board">
              <h2>Leaderboard</h2>
              
                 {renderTable}
              
          </div>
      
      ):null}
      
        
      </div>
         ): null }
      </div>
      
    
    </>
    
  );
};

export default App;