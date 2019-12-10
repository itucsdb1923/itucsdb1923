import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import MainTemplate from "./MainTemplate";
import { Card, CardColumns } from 'react-bootstrap';
import ListButton from "../components/ListButton";

const ListPage = (props) => {

  const [data, setData] = useState([]);

  console.log()

  useEffect(() => {
    let isCancelled = false;

    fetch("/api/list/" + props.match.params.list_id)
      .then(res => res.json())
      .then(data => {
        if (!isCancelled)
          setData(data)
      })
      .catch((error) => console.error(error));

    return () => { isCancelled = true };
  }, []);


  const items = <CardColumns style={{ margin: "20px", columnCount: 5 }}>
    {data.map((item) => {

      return (
        <Card bg="dark" text="white" key={item.item_id}>
          <Card.Img src={"/static/images/" + item.image} />
          <Card.Body>
            <Card.Title >{item.title}</Card.Title>
            <Card.Text>
              <Link as={Card.Link} to={"/" + item.item_type + "/" + item.item_id}>See More</Link>
            </Card.Text>
            <ListButton drop="up" itemId={item.item_id} itemType={item.item_type} />
          </Card.Body>
        </Card>
      )

    })}
  </CardColumns>

  return (
    <MainTemplate>
      {items}
    </MainTemplate>
  )
}

export default ListPage;
