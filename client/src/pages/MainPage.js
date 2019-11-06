import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import MainTemplate from "./MainTemplate";

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
    return (
      <div key={item.item_id}>
        {item.user}
        <br />
        {item.name}
        <hr />
      </div>)
  })

  return (
    <MainTemplate>
      {items}
    </MainTemplate>
  )
}


export default MainPage;
