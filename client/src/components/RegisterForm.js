import React, { useEffect, useState } from "react";
import { Form, Button } from "react-bootstrap";
import { Redirect } from "react-router-dom";

const RegisterForm = () => {

  const [state, setState] = useState({
    invalid: null,
    errorMessage: null,
    success: false
  });

  const handleSubmit = event => {
    event.preventDefault();

    let password1 = event.target.form[1].value;
    let password2 = event.target.form[2].value;

    if (password1 != password2) {
      setState({
        invalid: true,
        errorMessage: "Passwords don't match."
      });
    }
    else {


      fetch("/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: event.target.form[0].value,
          password: event.target.form[1].value
        }),
      })
        .then(response => {
          if (response.ok)
            setState({
              invalid: false,
              success: true
            });
          else
            setState({
              invalid: true,
              errorMessage: "User exists."
            });
        })
        .catch((error) => console.error(error))
    }
  }

  return (
    <Form>
      <Form.Group controlId="formBasicUsername">
        <Form.Label>Username</Form.Label>
        <Form.Control type="username" name="username" placeholder="Username" isInvalid={state.invalid} />
      </Form.Group>
      <Form.Group controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" name="password" placeholder="Password" isInvalid={state.invalid} />
      </Form.Group>
      <Form.Group controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" name="password2" placeholder="Password (Again)" isInvalid={state.invalid} />
        <Form.Control.Feedback type="invalid">
          {state.errorMessage}
        </Form.Control.Feedback>
      </Form.Group>
      <Button variant="primary" type="submit" onClick={e => handleSubmit(e)}>
        Submit
      </Button>
      <br />
      {state.success ? "Successful" : null}
    </Form>
  )
}


export default RegisterForm;
