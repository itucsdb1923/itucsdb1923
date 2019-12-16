import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import MainTemplate from "./MainTemplate";
import { Card, Button, Container, Row, Col } from 'react-bootstrap';
import List from "../components/List";
import ItemCard from "../components/ItemCard";
import NotLoggedInRedirect from "../components/NotLoggedInRedirect";

const ProfilePage = (props) => {

  const [state, setState] = useState({
    data: []
  });

  useEffect(() => {
    let isCancelled = false;

    fetch("/api/" + JSON.parse(localStorage.getItem("username")))
      .then(res => res.json())
      .then(data => {
        if (!isCancelled)
          setState({ data: data })
      })
      .catch((error) => console.error(error));

    return () => { isCancelled = true };
  }, []);

  const items = state.data.map((item) => {
    const subitems = item.items.map((subitem, index) => {
      return (
        <Col sm={3} lg={3} md={3} xl={3} key={index}>
          <ItemCard
            id={subitem.item_id}
            title={subitem.title}
            image={subitem.image}
            type={subitem.item_type} />
        </Col>
      )
    })

    return (
      <div key={item.list_id}>
        <Container>
          <br />
          <List name={item.name} user={item.user} list_id={item.list_id} showDelete>
            {subitems}
          </List>
        </Container>
      </div>)
  })

  return (
    <MainTemplate>
      <NotLoggedInRedirect >

        <div align="middle">
          <br />
          <Button variant="outline-secondary">
            <Link style={{
              color: "black",
              textDecoration: "none"
            }}
              to="/change_pw">
              Change Password
                </Link>
          </Button>
        </div>
        {items}
      </NotLoggedInRedirect>
    </MainTemplate>
  )
}


export default ProfilePage;
