import React, { useEffect, useState } from "react";
import { Form, Button } from "react-bootstrap";
import { Redirect } from "react-router-dom";

const ChangeForm = () => {

  const [loggedIn, setLoggedIn] = useState(null);
  const [redirect, setRedirect] = useState(false);
  const [invalid, setInvalid] = useState(null);

  useEffect(() => {
    let isCancelled = false;
    return () => { isCancelled = true };
  }, [])

  const handleSubmit = event => {
    event.preventDefault();

    fetch("/api/change_pw", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: event.target.form[0].value,
        password: event.target.form[1].value,
        new_password: event.target.form[2].value
      }),
    })
      .then(response => {
        if (response.ok)
          return response.json();
        else
          setInvalid(true);
      })
      .then(res => {

        setLoggedIn(true);
        setRedirect(true);

      })
      .catch((error) => console.error(error))
}
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
    <Form.Group controlId="formBasicPassword">
      <Form.Label>New Password</Form.Label>
      <Form.Control type="password" name="new_password" placeholder="New Password" isInvalid={invalid} />
    </Form.Group>
    <Form.Group controlId="formBasicPassword">
      <Form.Label>New Password</Form.Label>
      <Form.Control type="password" name="new_password_again" placeholder="New Password (Again)" isInvalid={invalid} />
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
  

  return null;
}


export default ChangeForm;
