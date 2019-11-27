import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import MainTemplate from "./MainTemplate";
import { Accordion, Card, Container, ProgressBar, Button } from 'react-bootstrap';

const ListPage = (props) => {

  const [state, setState] = useState({
    data: []
  });

  console.log()

  useEffect(() => {
    let isCancelled = false;

    fetch("/api/list/"+props.match.params.list_id)
      .then(res => res.json())
      .then(data => {
        if (!isCancelled)
          setState({ data: data })
      })
      .catch((error) => console.error(error));

    return () => { isCancelled = true };
  }, []);

  const items = state.data.map((item) => {
    return (
      <Card key={item.item_type + item.item_id}>
        <Accordion.Toggle as={Card.Header} eventKey={item.item_type + item.item_id} align="middle">
          {item.title}
        </Accordion.Toggle>
        <Accordion.Collapse eventKey={item.item_type + item.item_id}>
          <Card.Body>
            <Card.Title align = 'middle'>{item.item_type}</Card.Title>
          <div align="middle">
          <div style={{width : "50%"}}>
          {"Listist Score"}
          <ProgressBar now={item.score * 10}/>
          </div></div>
          <br />
          <div align="middle">
          <Button variant="primary">ADD</Button>
          </div>
          </Card.Body>
        </Accordion.Collapse>
      </Card>)
  })

  return (
    <MainTemplate>
      <br /><br />
      <Container>
        <Accordion defaultActiveKey="0">
          {items}
        </Accordion>
      </Container>
    </MainTemplate>
  )
}

export default ListPage;



