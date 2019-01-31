import axios from "axios";

//ACTION TYPES
const INITIALIZE = "INITIALIZE_MOVIE";

//ACTION CREATORS
const init = movies => ({ type: INITIALIZE, movies });

//REDUCERS
export default function reducer(movies = [], action) {
  switch (action.type) {
    case INITIALIZE:
      return action.movies;

    default:
      return movies;
  }
}

//THUNK CREATORS
export const fetchMovies = () => dispatch => {
  axios
    .get("/api/v1/search", {
      params: {
        query: "Harry Potter"
      }
    })
    .then(res => dispatch(init(res.data)))
    .then(res => console.log(res.data))
    .catch(err => console.error("Oh No! Could not find Campuses!", err));
};
