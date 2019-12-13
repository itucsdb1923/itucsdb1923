import React, { useState, useEffect } from "react";
import MainTemplate from "./MainTemplate";
import { CardColumns } from 'react-bootstrap';
import ItemCard from "../components/ItemCard";


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
        <ItemCard
          key={item.item_id}
          id={item.item_id}
          title={item.title}
          year={item.year}
          image={item.image}
          type="movie" />
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
