import React, { useEffect, useState } from "react";
import { Navbar, Nav, Dropdown } from "react-bootstrap";
import { Link } from "react-router-dom"

const Topbar = () => {
  const [loggedIn, setLoggedIn] = useState(null);
  const [username, setUser] = useState(null);

  useEffect(() => {
    if (JSON.parse(localStorage.getItem("loggedIn"))) {
      setLoggedIn(true);
      setUser(JSON.parse(localStorage.getItem("username")));

      if (new Date().getTime() >= JSON.parse(localStorage.getItem("exp"))) {
        fetch("/api/refresh", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + JSON.parse(localStorage.getItem("token"))
          },
        })
          .then(response => {
            if (response.ok)
              return response.json()
            else
              throw new Error("Something went wrong");
          })
          .then(res => {
            localStorage.setItem("exp", new Date().getTime() + (60 * 60 * 1000));
            localStorage.setItem("token", JSON.stringify(res.access_token));
          })
          .catch((error) => console.error(error))
      }

    }
  })

  return (
    <Navbar bg="light" expand="lg">
      <Link to="/" >
        <Navbar.Brand>Listist</Navbar.Brand>
      </Link>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Link to="/movies" className="nav-link">Movies</Link>
          <Link to="/books" className="nav-link">Books</Link>
          <Link to="/music" className="nav-link">Music</Link>
        </Nav>
        {loggedIn ? <Dropdown>
          <Dropdown.Toggle id="dropdown-basic">
            {username}
          </Dropdown.Toggle>

          <Dropdown.Menu>
            <Dropdown.Item onClick={() => {
              localStorage.removeItem("exp");
              localStorage.removeItem("loggedIn");
              localStorage.removeItem("token");
              localStorage.removeItem("username");
              setUser(null);
              setLoggedIn(false);
              location.reload();
            }}>Logout</Dropdown.Item>
            <Dropdown.Item>
              <Link to="/profile" style={{
                color: "black",
                textDecoration: "none",
              }}>Profile</Link>
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown> : <Navbar.Text><Link to="/register">Register</Link> / <Link to="/login">Login</Link></Navbar.Text>}
      </Navbar.Collapse>
    </Navbar>
  )
}

export default Topbar;