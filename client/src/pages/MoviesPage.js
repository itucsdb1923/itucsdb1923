import React, { useState, useEffect } from "react";
import MainTemplate from "./MainTemplate";
import { Card, CardColumns } from 'react-bootstrap';
import { Link } from "react-router-dom";
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


  const movies = <CardColumns style={{ margin: "20px", columnCount: 5}}>
    {state.data.map((item) => {

      return (
        <Card bg="dark" text="white" key={item.item_id}>
          <Card.Img src={"/static/images/" + item.image} />
          <Card.Body>
            <Card.Title >{item.title} ({item.year})</Card.Title>
            <Card.Text>
              <Link as={Card.Link} to={"/movie/" + item.item_id}>See More</Link>
            </Card.Text>
            <ListButton drop="up" itemId={item.item_id} itemType="movie" />
          </Card.Body>
        </Card>
      )

    })}
  </CardColumns>

  return (
    <MainTemplate>
      {movies}
    </MainTemplate>
  )
}

export default MoviePage;
