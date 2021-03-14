import { render, screen, fireEvent } from "@testing-library/react";
import Square from './Square';
import App from "./App";
import React from 'react';
import ReactDOM from 'react-dom';


test("renders without crashing", () => {
  const div = document.createElement("div"); 
  ReactDOM.render(<Square></Square>, div)
})

test("Test Next Player or Winner Button", () => {
  const result = render(<App />);
  
  const loginButtonElement = screen.getByText('Login');
  const inputUserNameE = screen.getByText('Username')
  
  
  expect(loginButtonElement).toBeInTheDocument();
  expect(inputUserNameE).toBeInTheDocument();

  
  fireEvent.click(loginButtonElement);
  expect(loginButtonElement).not.toBeInTheDocument();
  expect(inputUserNameE).not.toBeInTheDocument();
  
  const boardEAria = result.getByLabelText('board');
  expect(boardEAria).toBeInTheDocument();
  
  const squareEleAria = result.getByLabelText('Next/Winner');
  expect(squareEleAria).toBeInTheDocument();
  
  const infoWrapperElement = result.getByLabelText('infoWrapper');
  expect(infoWrapperElement).toBeInTheDocument();
  
  const scoreBoardElement = result.getByLabelText('RestartE');
  expect(scoreBoardElement).toBeInTheDocument();
  
});
