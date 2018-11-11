from app import db, ma


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.Integer)

    def __init__(self, title, author):
        self.title = title
        self.author = author


class BookSchema(ma.Schema):
    class Meta:
        fields = ('title', 'author')


book_schema = BookSchema()
books_schema = BookSchema(many=True)

# returns a readable book, the syntax is string format, '%r' is a placeholder for the
# book that will print and the '%' is saying format the self.title


def __repr__(self):
    return 'Book %r' % self.title
