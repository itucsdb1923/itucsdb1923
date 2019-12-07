import React, { useState, useEffect } from "react";
import { Dropdown, Button } from "react-bootstrap";
import { FiPlus, FiMinus } from "react-icons/fi";


const ListButton = ({ itemId, itemType, drop = "down" }) => {


  const [data, setData] = useState([]);
  const [loggedIn, setLoggedIn] = useState(null);




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
            setData(data)
          }
        })
        .catch((error) => console.error(error));

    }
    return () => { isCancelled = true };
  }, [])



  let itemClickHandler = (listId) => {

    let username = JSON.parse(localStorage.getItem("username"));
    fetch("/api/list/additem?" + "username=" + username + "&itemId=" + itemId +
      "&type=" + itemType + "&listId=" + listId, {
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + JSON.parse(localStorage.getItem("token"))
      },
    })
      .catch((error) => console.error(error));
  }


  let icon;


  let button = null;

  if (data.length != 0)
    button = (
      <Dropdown drop={drop}>
        <Dropdown.Toggle>
          Add to List
        </Dropdown.Toggle>
        <Dropdown.Menu>
          {data.map((list) => {

            icon = <FiPlus />;
            list.items.map((item) => {
              if (item.item_id == itemId && item.item_type == itemType)
                icon = <FiMinus />
            })

            return (
              <Dropdown.Item onClick={() => itemClickHandler(list.list_id)} key={list.list_id}>
                {icon} {list.name}
              </Dropdown.Item>
            )
          })}

          <Dropdown.Divider />
          <Dropdown.Item>Create New List</Dropdown.Item>
        </Dropdown.Menu>

      </Dropdown>

    );

  return button
}

export default ListButton;
