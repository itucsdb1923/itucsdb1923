import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import MainPage from "./pages/MainPage";
import MoviePage from "./pages/MoviePage";

render((
  <Router>
    <Switch>
      <Route exact path="/" component={MainPage} />
      <Route exact path="/login" component={LoginPage} />
      <Route exact path="/movies" component={MoviePage} />
      <Route exact path="*">404</Route>
    </Switch>
  </Router>
), document.getElementById('root'));
