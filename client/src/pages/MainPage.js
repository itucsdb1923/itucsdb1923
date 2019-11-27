import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import MainTemplate from "./MainTemplate";
import { Card, Button, Container } from 'react-bootstrap';

const MainPage = () => {

  const [state, setState] = useState({
    data: []
  });

  useEffect(() => {
    let isCancelled = false;

    fetch("/api")
      .then(res => res.json())
      .then(data => {
        if (!isCancelled)
          setState({ data: data })
      })
      .catch((error) => console.error(error));

    return () => { isCancelled = true };
  }, []);

  const items = state.data.map((item) => {
    if(item.items.length == 0){return}
    const subitems = item.items.map((subitem) => {
      return (
        <div class="col-sm-3">
      <Card style={{ width: '13rem'}}>
      <Card.Img variant="top" src="holder.js/100px180" />
        <Card.Body>
          <Card.Title>{subitem.title}</Card.Title>
          <Card.Text>
            {subitem.item_type}
          </Card.Text>
        </Card.Body>
      </Card></div>
      )})

    return (
      <div key={item.list_id}>
      <Container>  
      <br/>
        <Card>
          <Card.Header><div class="row"><div class="col-sm-6"><h3>{item.name}</h3></div><div class="col-sm-6" align="right"><h5>{item.user}</h5></div></div></Card.Header>
          <Card.Body>
            <Card.Text align="middle" >
              <div class="row">
                {subitems}
              </div>
            </Card.Text>
            <div align="right">
              <Card.Link href={"list/" + item.list_id}>See All Contents</Card.Link>
              <br/><br/>
              <Card.Subtitle className="mb-2 text-muted"><h6>{item.date}</h6></Card.Subtitle>
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
