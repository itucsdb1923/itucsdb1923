import React, { useState, useEffect } from "react";
import MainTemplate from "./MainTemplate";
import { Container, Jumbotron, Image, Row, Col } from "react-bootstrap";
import Rating from "react-star-ratings";
import ListButton from "../components/ListButton";

export default (props) => {


  const [data, setData] = useState({});

  useEffect(() => {
    let isCancelled = false;

    fetch("/api/movie/" + props.match.params.movie_id)
      .then(res => res.json())
      .then(fetchedData => {
        if (!isCancelled)
          setData(fetchedData);
      })
      .catch((error) => console.error(error));

    return () => { isCancelled = true };
  }, []);


  let castList;

  if (data.cast != undefined) {
    castList = <ul>{data.cast.map((person, index) => <li key={index}>{person}</li>)}</ul>
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
                <b>Director:</b> {data.director}
                <br />
                <b>Year:</b> {data.year}
                <br />
                <b>IMDB:</b> {data.imdb_score}
                <br />
                <b>Cast:</b> {castList}
                <br/>
                <ListButton itemId={data.item_id} drop="right" itemType="book" />
            </Col>
          </Row>
        </Container>
      </Jumbotron>
    </MainTemplate>
  );
}