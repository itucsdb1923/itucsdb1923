import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import MainTemplate from "./MainTemplate";
import { Card, Container, Row, Col } from 'react-bootstrap';
import ItemCard from "../components/ItemCard";

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
          <Card>
            <Card.Header>
              <Row>
                <Col><h4>{item.name}</h4></Col>
                <Col align="right"><h5>@{item.user}</h5></Col>
              </Row>
            </Card.Header>
            <Card.Body>
              <Row>
                {subitems}
              </Row>
              <div align="right">
                <Link to={"list/" + item.list_id}>See All Contents</Link>
              </div>
            </Card.Body>
          </Card>
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
