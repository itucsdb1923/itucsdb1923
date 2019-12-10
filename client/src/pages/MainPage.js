import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import MainTemplate from "./MainTemplate";
import { Card, Container, Row, Col } from 'react-bootstrap';

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
          <Card bg="dark" text="white">
            <Card.Img src={"/static/images/" + subitem.image} />
            <Card.Body>
              <Card.Title>{subitem.title}</Card.Title>
              <Card.Text>
                {subitem.item_type}
              </Card.Text>
            </Card.Body>
          </Card>
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
