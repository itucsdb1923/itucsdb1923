import React from "react";
import Topbar from "../components/Topbar"


const MainTemplate = (props) => {

  // refresh token
  return (
    <div>
      <Topbar />
      {props.children}
    </div>
  )
}

export default MainTemplate;
