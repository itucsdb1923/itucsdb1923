import React from "react";
import LoginForm from "../components/LoginForm";
import { Container } from "react-bootstrap";
import Maintemplate from "./MainTemplate";
import LoggedInRedirect from "../components/LoggedInRedirect";

const LoginPage = () => {



  return (
    <Maintemplate>
      <Container>
        <LoggedInRedirect>
          <LoginForm />
        </LoggedInRedirect>
      </Container>
    </Maintemplate>
  )
}


export default LoginPage;
