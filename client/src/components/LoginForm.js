import React, { useEffect, useState } from "react";
import { Form, Button } from "react-bootstrap";
import { Redirect } from "react-router-dom";

const LoginForm = () => {

  const [loggedIn, setLoggedIn] = useState(null);
  const [redirect, setRedirect] = useState(false);
  const [invalid, setInvalid] = useState(null);

  useEffect(() => {
    let isCancelled = false;
    if (!isCancelled) {
      if (JSON.parse(localStorage.getItem("loggedIn"))) {
        setLoggedIn(true);
        setTimeout(() => {
          setRedirect(true);
        }, 1500);
      }
      else
        setLoggedIn(false);
    }
    return () => { isCancelled = true };
  }, [])

  const handleSubmit = event => {
    event.preventDefault();

    fetch("/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: event.target.form[0].value,
        password: event.target.form[1].value
      }),
    })
      .then(response => {
        if (response.ok)
          return response.json();
        else
          setInvalid(true);
      })
      .then(res => {

        localStorage.setItem("exp", new Date().getTime() + (60 * 60 * 1000));
        localStorage.setItem("token", JSON.stringify(res.access_token));
        localStorage.setItem("loggedIn", JSON.stringify(true));
        localStorage.setItem("username", JSON.stringify(res.username));
        setLoggedIn(true);
        setRedirect(true);

      })
      .catch((error) => console.error(error))
  }

  if (loggedIn != null) {

    if (loggedIn)
      return (
        <div>
          You're already logged in. Redirecting to the main page.
          {redirect ? <Redirect to="/" /> : null}
        </div>)
    else
      return (
        <Form>
          <Form.Group controlId="formBasicUsername">
            <Form.Label>Username</Form.Label>
            <Form.Control type="username" name="username" placeholder="Username" isInvalid={invalid} />
          </Form.Group>
          <Form.Group controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" name="password" placeholder="Password" isInvalid={invalid} />
            <Form.Control.Feedback type="invalid">
              Invalid username or password
            </Form.Control.Feedback>
          </Form.Group>
          {/*<Form.Group controlId="formBasicCheckbox">
            <Form.Check type="checkbox" label="Check me out" />
          </Form.Group>*/}
          <Button variant="primary" type="submit" onClick={e => handleSubmit(e)}>
            Submit
          </Button>
          <br />
        </Form>
      )
  }

  return null;
}


export default LoginForm;
