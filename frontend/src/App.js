import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import axios from "axios";

class App extends Component {
  componentDidMount() {
    axios
      .get("/api/v1/search", {
        params: {
          query: "Harry Potter"
        }
      })
      .then(res => console.log(res.data))
      .catch(err => console.error("Oh No! Could not find Campuses!", err));
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>Movie Review Project</p>
        </header>
      </div>
    );
  }
}

export default App;
