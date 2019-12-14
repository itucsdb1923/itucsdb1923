import React, { useState, useEffect } from "react";
import { Dropdown, Button, Modal, Form } from "react-bootstrap";
import { FiPlus, FiMinus } from "react-icons/fi";


const ListButton = ({ itemId, itemType, drop = "down" }) => {

  const [data, setData] = useState([]);
  const [isInLists, setInLists] = useState([]);
  const [modalShow, setModalShow] = useState(false);

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
  }

  let handleCreate = e => {
    event.preventDefault();

    let username = JSON.parse(localStorage.getItem("username"));
    fetch("/api/createlist?" + "username=" + username + "&name=" + e.target[0].value, {
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + JSON.parse(localStorage.getItem("token"))
      },
    })
      .catch((error) => console.error(error));

    setModalShow(false);
  }

  let button = null;

  if (JSON.parse(localStorage.getItem("loggedIn")))
    button = (
      <Dropdown drop={drop} onClick={()=>{fetchUserLists()}}>
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
          <Dropdown.Divider />
          <Dropdown.Item onClick={() => { setModalShow(true) }}>
            Create List
          </Dropdown.Item>

          <Modal
            size="lg"
            aria-labelledby="contained-modal-title-vcenter"
            centered
            show={modalShow}
            onHide={() => { setModalShow(false) }}
          >
            <Modal.Header closeButton>
              <Modal.Title id="contained-modal-title-vcenter">
                Create New List
              </Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <Form onSubmit={e => handleCreate(e)}>
                <Form.Group controlId="formBasicUsername">
                  <Form.Control placeholder="List Name" />
                </Form.Group>

                <Button variant="primary" type="submit">
                  Create
                </Button>
                <br />
              </Form>
            </Modal.Body>

          </Modal>

        </Dropdown.Menu>
      </Dropdown>

    );

  return button
}

export default ListButton;
