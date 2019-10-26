import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { Button } from "react-bootstrap";

render((
  <Router>
    <div>
      <Route exact path="/">Main Page</Route>
      <Route path="/users">Users</Route>
      <Route path="/contact">Contact</Route>
      <Route path="/button">
        <Button>
          Button Example
        </Button>
      </Route>
    </div>
  </Router>
), document.getElementById('root'));

