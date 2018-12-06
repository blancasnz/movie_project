from flask import jsonify, abort, request
from models import Book, book_schema, books_schema
from app import app, db
from movie_db import search


@app.route("/api/v1/search", methods=['GET'])
def get_results():
    query = request.args.get('query')
    movies = search(query)
    movie_response = []
    for movie in movies:
        movie_response.append(movie.to_dictionary())
    return jsonify(movie_response)


# @app.route("/api/movie", methods=['POST'])
# def add_book():
#     title = request.json['title']
#     author = request.json['author']

#     new_book = Book(title, author)

#     db.session.add(new_book)
#     db.session.commit()

#     return book_schema.jsonify(new_book)
