import React, { useState, useEffect } from "react";
import MainTemplate from "./MainTemplate";
import { Container, Jumbotron, Image, Row, Col } from "react-bootstrap";
import Rating from "react-star-ratings";
import ListButton from "../components/ListButton";

export default (props) => {


  const [data, setData] = useState({});

  useEffect(() => {
    let isCancelled = false;

    fetch("/api/book/" + props.match.params.book_id)
      .then(res => res.json())
      .then(fetchedData => {
        if (!isCancelled)
          setData(fetchedData);
      })
      .catch((error) => console.error(error));

    return () => { isCancelled = true };
  }, []);


  let genres;

  if (data.genre != undefined) {
    genres = <ul>{data.genre.map((item, index) => <li key={index}>{item}</li>)}</ul>
  }


  return (
    <MainTemplate>
      <Jumbotron fluid>
        <Container>
          <Row>
            <Col md="4" lg="4" xl="4">
              <Image fluid src={"/static/images/" + data.image} />
            </Col>
            <Col>

              <h1>{data.title} <small className="text-muted">({data.year})</small></h1>

              <Rating rating={data.score}
                numberOfStars={10}
                starDimension="40px"
                starSpacing="5px"
                starRatedColor="gold" />
              <br /><br />
              <p>
                {data.description}
              </p>
              <b>Author:</b> {data.author}
              <br />
              <b>Year:</b> {data.year}
              <br />
              <b>Pages:</b> {data.page_num}
              <br />
              <b>Genre:</b> {genres}
              <br />
              <ListButton itemId={data.item_id} drop="right" itemType="music" />
            </Col>
          </Row>
        </Container>
      </Jumbotron>
    </MainTemplate>
  );
}