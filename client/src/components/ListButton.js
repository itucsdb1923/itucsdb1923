import React, { useState, useEffect } from "react";
import { Dropdown, Button } from "react-bootstrap";
import { FiPlus, FiMinus } from "react-icons/fi";




const ListButton = ({ itemId, itemType, drop = "down" }) => {

  const [data, setData] = useState([]);
  const [isInLists, setInLists] = useState([]);

  useEffect(() => {
    let isCancelled = false;
    fetchUserLists(isCancelled);

    return () => { isCancelled = true };
  }, [])


  let fetchUserLists = (isCancelled = false) => {
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
            setInLists(data.map((list) => {
              let exists = false;
              list.items.map(item => {
                if (item.item_id == itemId && item.item_type == itemType) exists = true;
              })
              return exists;
            }))
          }
        })
        .catch((error) => console.error(error));
    }
  }


  let addRemove = (listId, remove = false) => {

    let operation = (remove ? "remove" : "add") + "item"

    let username = JSON.parse(localStorage.getItem("username"));
    fetch("/api/list/" + operation + "?" + "username=" + username + "&itemId=" + itemId +
      "&type=" + itemType + "&listId=" + listId, {
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + JSON.parse(localStorage.getItem("token"))
      },
    })
      .catch((error) => console.error(error));

    fetchUserLists();
  }

  let button = null;

  if (JSON.parse(localStorage.getItem("loggedIn")))
    button = (
      <Dropdown drop={drop}>
        <Dropdown.Toggle>
          Add to List
        </Dropdown.Toggle>
        <Dropdown.Menu>
          {data.map((list, index) => {

            let onClick = () => { addRemove(list.list_id) };
            let icon = <FiPlus />;

            if (isInLists[index]) {
              icon = <FiMinus />;
              onClick = () => { addRemove(list.list_id, true) };
            }

            return (
              <Dropdown.Item onClick={onClick} key={list.list_id}>
                {icon} {list.name}
              </Dropdown.Item>
            )
          })}

        </Dropdown.Menu>
      </Dropdown>

    );

  return button
}

export default ListButton;
