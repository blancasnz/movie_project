from flask import jsonify, abort, request
from app import app

movies = [
  {
    'title': 'Scott Pilgrim',
    'year' : 2010
  },
  {
    'title': 'Harry Potter',
    'year' : 2000
  },
  {
    'title': 'Swiss Army Man',
    'year' : 2017
  }
]

@app.route("/api/movies", methods=['GET'])
def get_movies():
  return jsonify({'movies': movies})


@app.route("/api/movies", methods=['POST'])
def add_movies():
  if not request.json or not 'title' in request.json:
    abort(400)
  movie = {
    'title': request.json['title'],
    'year' : request.json['year']
  }
  movies.append(movie)
  return jsonify({'movie': movie}), 201

if __name__ == '__main__':
  app.run(debug=True)
