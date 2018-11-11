from flask import jsonify, abort, request
from models import Book, book_schema, books_schema
from app import app, db

movies = [
    {
        'title': 'Scott Pilgrim',
        'year': 2010
    },
    {
        'title': 'Harry Potter',
        'year': 2000
    },
    {
        'title': 'Swiss Army Man',
        'year': 2017
    }
]


@app.route("/api/movies", methods=['GET'])
def get_movies():
    return jsonify({'movies': movies})


@app.route("/api/book", methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']

    new_book = Book(title, author)

    db.session.add(new_book)
    db.session.commit()

    return book_schema.jsonify(new_book)


if __name__ == '__main__':
    app.run(debug=True)
