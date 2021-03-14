import { render, screen, fireEvent } from "@testing-library/react";
import App from "./App";

test("Test if shows Board", () => {
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
  
  const enjoyBElement = result.getByLabelText('Enjoy');
  expect(enjoyBElement).toBeInTheDocument();
  
  
});