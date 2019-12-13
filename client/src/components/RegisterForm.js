import React, { useEffect, useState } from "react";
import { Form, Button } from "react-bootstrap";
import { Redirect } from "react-router-dom";

const RegisterForm = () => {

  let [invalid, setInvalid] = useState(null);
  let [errorMessage, setErrorMessage] = useState(null);
  let [success, setSuccess] = useState(false);
  let [redirect, setRedirect] = useState(false);

  const handleSubmit = event => {
    event.preventDefault();

    let password1 = event.target.form[1].value;
    let password2 = event.target.form[2].value;

    if (password1 != password2) {
      setErrorMessage("Password don't match");
      setInvalid(true);
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
          if (response.ok) {
            setInvalid(false);
            setSuccess(true);
            setTimeout(() => {
              setRedirect(true);
            }, 2000);
          }
          else {
            setInvalid(true);
            setErrorMessage("User exists");
          }
        })
        .catch((error) => console.error(error))
    }
  }

  return (
    <Form>
      {success ? "User created. Redirecting to login page." : null}
      {redirect ? <Redirect to="/login" /> : null}
      <Form.Group controlId="formBasicUsername">
        <Form.Label>Username</Form.Label>
        <Form.Control type="username" name="username" placeholder="Username" isInvalid={invalid} />
      </Form.Group>
      <Form.Group controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" name="password" placeholder="Password" isInvalid={invalid} />
      </Form.Group>
      <Form.Group controlId="formBasicPassword2">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" name="password2" placeholder="Password (Again)" isInvalid={invalid} />
        <Form.Control.Feedback type="invalid">
          {errorMessage}
        </Form.Control.Feedback>
      </Form.Group>
      <Button variant="primary" type="submit" onClick={e => handleSubmit(e)}>
        Submit
      </Button>
      <br />
    </Form>
  )
}


export default RegisterForm;
