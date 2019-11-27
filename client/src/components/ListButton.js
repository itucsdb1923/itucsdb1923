import React, { useState, useEffect } from "react";
import { Dropdown } from "react-bootstrap";

const ListButton = (props) => {

  const [state, setState] = useState({
    data: [],
    loggedIn: null,
  });


  useEffect(() => {
    let isCancelled = false;

    if (JSON.parse(localStorage.getItem("loggedIn"))) {
      fetch("/api/user/" + JSON.parse(localStorage.getItem("username")) + "/lists", {
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + JSON.parse(localStorage.getItem("token"))
        },

      })
        .then(res => res.json())
        .then(data => {
          if (!isCancelled) {
            setState({ data: data })
          }
        })
        .catch((error) => console.error(error));

    }
    return () => { isCancelled = true };
  }, [])





  let itemClickHandler = (listId) => {

    let username = JSON.parse(localStorage.getItem("username"));
    fetch("/api/list/additem?" + "username=" + username + "&itemId=" + props.item.itemId +
      "&type=" + props.item.type + "&listId=" + listId, {
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + JSON.parse(localStorage.getItem("token"))
      },

    })
      .then(res => res.json())
      .then(data => {
        console.log(data);
      })
      .catch((error) => console.error(error));
  }



  let button = null;

  if (state.data.length != 0)
    button = (
      <Dropdown>
        <Dropdown.Toggle id="dropdown-basic">
          Add to List
        </Dropdown.Toggle>

        <Dropdown.Menu>
          {state.data.map((list) => {
            return (
              <Dropdown.Item onClick={() => itemClickHandler(list.list_id)} key={list.list_id}>
                {list.name}
              </Dropdown.Item>
            )
          })}
        </Dropdown.Menu>
      </Dropdown>

    );

  return button

}

export default ListButton;
