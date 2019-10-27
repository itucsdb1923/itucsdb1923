import React from "react";

class MoviePage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    render() {
        let { movie_id } = useParams();
        return <div>{movie_id}</div>
    }
}

export default MoviePage;