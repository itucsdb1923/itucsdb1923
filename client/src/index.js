import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import MainPage from "./pages/MainPage";
import MoviePage from "./pages/MoviePage";
import BookPage from "./pages/BookPage";
import MusicPage from "./pages/MusicPage";
import ListPage from "./pages/ListPage";
import ProfilePage from "./pages/ProfilePage";
import ChangePage from "./pages/ChangePage";


render((
  <Router>
    <Switch>
      <Route exact path="/" component={MainPage} />
      <Route exact path="/login" component={LoginPage} />
      <Route exact path="/movies" component={MoviePage} />
      <Route exact path="/books" component={BookPage} />
      <Route exact path="/music" component={MusicPage} />
      <Route exact path="/list/:list_id" component={ListPage} />
      <Route exact path="/user/:username" component={ProfilePage} />
      <Route exact path="/change_pw" component={ChangePage} />
      <Route exact path="*">404</Route>
    </Switch>
  </Router>
), document.getElementById('root'));
