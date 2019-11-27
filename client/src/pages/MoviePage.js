import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import MainTemplate from "./MainTemplate";
import { Accordion, Card, Container, ProgressBar, Button } from 'react-bootstrap';
import ListButton from "../components/ListButton";

const MoviePage = (props) => {

  const [state, setState] = useState({
    data: [],
  });

  useEffect(() => {
    let isCancelled = false;

    fetch("/api/movies")
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
      <Card key={item.item_id}>
        <Accordion.Toggle as={Card.Header} eventKey={item.item_id} align="middle">
          {item.title + " (" + item.year + ")"}
        </Accordion.Toggle>
        <Accordion.Collapse eventKey={item.item_id}>
          <Card.Body>
            <Card.Title>{item.director}</Card.Title>
            <Card.Text>
              {"CAST : " + item.cast}
              <br />
              {"DESCRIPTION : " + item.description}
              <br />
            </Card.Text>
            <div align="middle">
              <div style={{ width: "50%" }}>
                {"Listist Score"}
                <ProgressBar now={item.score * 10} label={`${item.score + " (" + item.votes + ")"}`} />
                {"Imdb Score"}
                <ProgressBar variant="warning" now={item.imdb_score * 10} label={`${item.imdb_score}`} />
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
      <br />
      <Container>
        <Accordion defaultActiveKey="0">
          {items}
        </Accordion>
      </Container>
      <ListButton item={{
        itemId: 1,
        type: "BOOK"
      }} />
    </MainTemplate>
  )
}

export default MoviePage;



