import { render, screen, fireEvent } from "@testing-library/react";
import App from "./App";
import React from 'react';
import ReactDOM from 'react-dom';


test("renders without crashing", () => {
  const div = document.createElement("div"); 
  ReactDOM.render(<App />, div)
});

test("Show and H Login", () => {
  const result = render(<App />);
  
  const loginButtonElement = screen.getByText('Login');
  
  expect(loginButtonElement).toBeInTheDocument();
  
  fireEvent.click(loginButtonElement);
  expect(loginButtonElement).not.toBeInTheDocument();
  
});
test("Test if login button and input hide", () => {
  const result = render(<App />);
  
  const loginButtonElement = screen.getByText('Login');
  const inputUserNameE = screen.getByText('Username') 
  
  expect(loginButtonElement).toBeInTheDocument();
  expect(inputUserNameE).toBeInTheDocument();
  
  fireEvent.click(loginButtonElement);
  expect(loginButtonElement).not.toBeInTheDocument();
  expect(inputUserNameE).not.toBeInTheDocument();
  
});