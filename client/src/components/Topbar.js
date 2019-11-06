import React, { useEffect, useState } from "react";
import { Navbar, Nav, Form, FormControl, Button } from "react-bootstrap";
import { Link } from "react-router-dom"

const Topbar = () => {
  const [loggedIn, setLoggedIn] = useState(null);
  const [username, setUser] = useState(null);

  useEffect(() => {
    if (JSON.parse(localStorage.getItem("loggedIn"))) {
      setLoggedIn(true);
      setUser(JSON.parse(localStorage.getItem("username")));
    }
  })

  return (
    <Navbar bg="light" expand="lg">
      <Link to="/" ><Navbar.Brand>
        Listist
        </Navbar.Brand></Link>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Navbar.Text><Link to="/movies">Movies</Link></Navbar.Text>
          <Navbar.Text><Link to="/books">Books</Link></Navbar.Text>
          <Navbar.Text><Link to="/music">Music</Link></Navbar.Text>
        </Nav>
        {loggedIn ? username : <Navbar.Text><Link to="/login">Login</Link></Navbar.Text>}
      </Navbar.Collapse>
    </Navbar>
  )
}

export default Topbar;