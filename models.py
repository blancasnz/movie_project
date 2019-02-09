from app import db


class User(db.Model):
    _tablename_ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    bio = db.Column(db.String(50))
    email = db.Column(db.String(), nullable=False)

    def __init__(self, name, bio, email):
        self.name = name
        self.bio = bio
        self.email = email

    def __repr__(self):
        return 'id {}'.format(self.id)
