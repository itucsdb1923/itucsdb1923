import React from "react";
import { Card } from "react-bootstrap";

const List = (props) => {


  return (
    <Card className="mb-3">
      <Card.Header>{props.data.name}</Card.Header>
      <Card.Body>{props.children}</Card.Body>
      <Card.Footer>@{props.data.user}</Card.Footer>
    </Card>
  )
}


export default List;
