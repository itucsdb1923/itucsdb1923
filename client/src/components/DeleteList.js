import React, { useState } from 'react';
import { Button } from "react-bootstrap";
import { Redirect } from 'react-router-dom';


export default ({ listId }) => {

  let [isDeleted, setDelete] = useState(false);

  let handleClick = () => {
    let username = JSON.parse(localStorage.getItem("username"));
    fetch("/api/deletelist?" + "username=" + username + "&listId=" + listId, {
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + JSON.parse(localStorage.getItem("token"))
      },
    })
      .catch((error) => console.error(error));
    setDelete(true);
  }


  let button = null;

  if (JSON.parse(localStorage.getItem("loggedIn")))
    button = (
      <div>
        {isDeleted ? <Redirect to="/" /> : null}
        <Button onClick={handleClick} variant="danger">
          Delete List
        </Button>
      </div>
    )

  return button;
}