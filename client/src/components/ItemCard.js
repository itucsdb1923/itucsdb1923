import React from "react";
import { Card } from "react-bootstrap";
import ListButton from "./ListButton";
import { Link } from "react-router-dom";

export default ({ type, image, title, year, id, }) => (
  <Card bg="dark" text="white">
    <Card.Img src={"/static/images/" + image} />
    <Card.Body>
      <Card.Title >{title} {year != null ? "(" + year + ")" : null}</Card.Title>
      <Card.Text>
        <Link as={Card.Link} to={"/" + type + "/" + id}>See More</Link>
      </Card.Text>
      <ListButton drop="up" itemId={id} itemType={type} />
    </Card.Body>
  </Card>
);