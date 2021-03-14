import { render, screen, fireEvent } from "@testing-library/react";
import App from "./App";



test("Show and H Login", () => {
  const result = render(<App />);
  
  const loginButtonElement = screen.getByText('Login');
  // const alertMsgElement = scren.getByText('Alert')
  expect(loginButtonElement).toBeInTheDocument();
  
  fireEvent.click(loginButtonElement);
  expect(loginButtonElement).not.toBeInTheDocument();
  // expect(alertMsgElement).toBeInTheDocument();
  
});
