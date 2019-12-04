import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import MainPage from "./pages/MainPage";
import MoviesPage from "./pages/MoviesPage";
import MoviePage from "./pages/MoviePage";
import BookPage from "./pages/BookPage";
import BooksPage from "./pages/BooksPage";
import MusicPage from "./pages/MusicPage";
import AllMusicPage from "./pages/AllMusicPage";
import ListPage from "./pages/ListPage";
import RegisterPage from "./pages/RegisterPage";

render((
  <Router>
    <Switch>
      <Route exact path="/" component={MainPage} />
      <Route exact path="/login" component={LoginPage} />
      <Route exact path="/register" component={RegisterPage} />
      <Route exact path="/movies" component={MoviesPage} />
      <Route exact path="/movie/:movie_id" component={MoviePage} />
      <Route exact path="/books" component={BooksPage} />
      <Route exact path="/book/:book_id" component={BookPage} />
      <Route exact path="/music" component={AllMusicPage} />
      <Route exact path="/music/:music_id" component={MusicPage} />
      <Route exact path="/list/:list_id" component={ListPage} />
      <Route exact path="*">404</Route>
    </Switch>
  </Router>
), document.getElementById('root'));
