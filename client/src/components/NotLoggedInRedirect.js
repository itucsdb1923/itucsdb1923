import React, { useEffect, useState } from "react";
import { Redirect } from "react-router-dom";

const NotLoggedInRedirect = ({
  timeout = 2,
  message = "You are already not logged in.",
  children }) => {

  const [loggedIn, setLoggedIn] = useState(null);
  const [redirect, setRedirect] = useState(false);

  useEffect(() => {
    let isCancelled = false;
    if (!isCancelled) {
      if (JSON.parse(localStorage.getItem("loggedIn"))) {
        setLoggedIn(true);
      }
      else {
        setTimeout(() => {
          setRedirect(true);
        }, timeout * 1000);

        setLoggedIn(false);
      }
    }
    return () => { isCancelled = true };
  }, [])



  if (!loggedIn || loggedIn == null)
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


  return null;
}


export default NotLoggedInRedirect;
