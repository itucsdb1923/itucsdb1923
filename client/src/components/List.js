import React from "react";
import { Card, Row, Col } from "react-bootstrap";
import { Link } from "react-router-dom";
import DeleteList from "../components/DeleteList"

const List = ({ name, user, list_id, children, showDelete = false }) => {


  return (
    <Card>
      <Card.Header>
        <Row>
          <Col><h4>{name}</h4></Col>
          <Col align="right"><h5>@{user}</h5></Col>
        </Row>
      </Card.Header>
      <Card.Body>
        <Row>
          {children}
        </Row>
        <div align="right">
          <Link to={"list/" + list_id}>See All Contents</Link>
        </div>
      </Card.Body>
      {showDelete ? <Card.Footer><DeleteList listId={list_id} /></Card.Footer> : null}
    </Card>
  )
}


export default List;
