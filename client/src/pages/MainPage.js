import React, { useState, useEffect } from "react";
import MainTemplate from "./MainTemplate";
import {  Container,  Col } from 'react-bootstrap';
import ItemCard from "../components/ItemCard";
import List from "../components/List";

const MainPage = () => {

  const [data, setData] = useState([]);

  useEffect(() => {
    let isCancelled = false;

    fetch("/api")
      .then(res => res.json())
      .then(data => {
        if (!isCancelled)
          setData(data);
      })
      .catch((error) => console.error(error));

    return () => { isCancelled = true };
  }, []);

  const items = data.map((item) => {
    if (item.items.length == 0) { return }
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
          <List name={item.name} user={item.user} list_id={item.list_id}>
            {subitems}
          </List>
        </Container>
      </div>)
  })

  return (
    <MainTemplate>
      {items}
    </MainTemplate>
  )
}


export default MainPage;
