import React, { Component } from "react";
// import logo from "./logo.svg";
// import store from "../store";
import "../App.css";
import { fetchMovies } from "../reducers/movies";

class App extends Component {
  componentDidMount() {
    const movieThunk = fetchMovies();
    // store.dispatch(movieThunk);
    //     axios
    //       .get("/api/v1/search", {
    //         params: {
    //           query: "Harry Potter"
    //         }
    //       })
    //       .then(res => console.log(res.data))
    //       .catch(err => console.error("Oh No! Could not find Campuses!", err));
  }

  render() {
    return (
      <div className="App">
        <main>
          <p>Movie Review Project</p>
        </main>
      </div>
    );
  }
}

export default App;
