import React, { useState, useEffect } from "react";
import MainTemplate from "./MainTemplate";
import {CardColumns } from 'react-bootstrap';
import ItemCard from "../components/ItemCard";


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
        <ItemCard
        key={item.item_type + item.item_id}
        id={item.item_id}
        title={item.title}
        image={item.image}
        type={item.item_type} />
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
