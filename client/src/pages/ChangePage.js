import React from "react";
import ChangeForm from "../components/ChangeForm";
import { Container } from "react-bootstrap";
import Maintemplate from "./MainTemplate";

const ChangePage = () => {
  


  return (
    <Maintemplate>
      <Container>
        <ChangeForm />
      </Container>
    </Maintemplate>
  )
}


export default ChangePage;