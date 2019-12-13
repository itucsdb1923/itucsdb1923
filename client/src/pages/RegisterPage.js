import React from "react";
import RegisterForm from "../components/RegisterForm";
import LoggedInRedirect from "../components/LoggedInRedirect";
import { Container } from "react-bootstrap";
import Maintemplate from "./MainTemplate";

const RegisterPage = () => {



  return (
    <Maintemplate>
      <Container>
        <LoggedInRedirect message="You are already a user. Redirecting to the home page.">
          <br/>
          <h3>Register</h3>
          <br />
          <RegisterForm />
        </LoggedInRedirect>
      </Container>
    </Maintemplate>
  )
}


export default RegisterPage;
