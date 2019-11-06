import React from "react";
import LoginForm from "../components/LoginForm";
import { Container } from "react-bootstrap";
import Maintemplate from "./MainTemplate";

const LoginPage = () => {
  


  return (
    <Maintemplate>
      <Container>
        <LoginForm />
      </Container>
    </Maintemplate>
  )
}


export default LoginPage;
