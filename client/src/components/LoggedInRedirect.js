import React, { useEffect, useState } from "react";
import { Redirect } from "react-router-dom";

const LoggedInRedirect = ({
  timeout = 2,
  message = "You are already logged in. Redirecting to the main page.",
  children }) => {

  const [loggedIn, setLoggedIn] = useState(null);
  const [redirect, setRedirect] = useState(false);

  useEffect(() => {
    let isCancelled = false;
    if (!isCancelled) {
      if (JSON.parse(localStorage.getItem("loggedIn"))) {
        setLoggedIn(true);
        setTimeout(() => {
          setRedirect(true);
        }, timeout * 1000);
      }
      else
        setLoggedIn(false);
    }
    return () => { isCancelled = true };
  }, [])


  if (loggedIn != null) {

    if (loggedIn)
      return (
        <div>
          {message}
          {redirect ? <Redirect to="/" /> : null}
        </div>)
    else
      return (
        <div>
          {children}
        </div>
      )
  }

  return null;
}


export default LoggedInRedirect;
