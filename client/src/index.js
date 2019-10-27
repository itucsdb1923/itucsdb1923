import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { Button } from "react-bootstrap";
import MoviePage from "./pages/MoviePage";


render((
  <Router>
    <div>
      <Switch>
        <Route path="movie/:movie_id"><MoviePage /></Route>
      </Switch>
    </div>
  </Router>
), document.getElementById('root'));

