import React from "react";

const MoviePage = (props) => {
    return <div>{props.match.params.movie_id}</div>
}

export default MoviePage;