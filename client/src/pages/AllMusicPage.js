import React, { useState, useEffect } from "react";
import MainTemplate from "./MainTemplate";
import { CardColumns } from 'react-bootstrap';
import ItemCard from "../components/ItemCard";


export default (props) => {

  const [state, setState] = useState({
    data: [],
  });

  useEffect(() => {
    let isCancelled = false;

    fetch("/api/music")
      .then(res => res.json())
      .then(data => {
        if (!isCancelled)
          setState({ data: data })
      })
      .catch((error) => console.error(error));

    return () => { isCancelled = true };
  }, []);


  const allMusic = <CardColumns style={{ margin: "20px", columnCount: 5 }}>
    {state.data.map((item) => {

      return (
        <ItemCard
          key={item.item_id}
          id={item.item_id}
          title={item.title}
          year={item.year}
          image={item.image}
          type="music" />
      )

    })}
  </CardColumns>

  return (
    <MainTemplate>
      {allMusic}
    </MainTemplate>
  )
}

