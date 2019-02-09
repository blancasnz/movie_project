from flask import jsonify, abort, request
# from models import Book, book_schema, books_schema
from app import app, db
from movie_db import search
from models import User


@app.route("/api/v1/search", methods=['GET'])
def get_results():
    query = request.args.get('query')
    movies = search(query)
    movie_response = []
    for movie in movies:
        movie_response.append(movie.to_dictionary())
    return jsonify(movie_response)


@app.route("/api/v1/profile", methods=['GET'])
def get_profile():
    reviews = [
        {
            'image': 'IMG_2196.JPG',
            'review_text': 'It was aight',
            'rating': '3 stars'
        },
        {
            'image': 'IMG_2196.JPG',
            'review_text': 'I loved it',
            'rating': '5 stars'
        }
    ]
    return jsonify(reviews)


# @app.route("/api/movie", methods=['POST'])
# def add_book():
#     title = request.json['title']
#     author = request.json['author']

#     new_book = Book(title, author)

#     db.session.add(new_book)
#     db.session.commit()

#     return book_schema.jsonify(new_book)
