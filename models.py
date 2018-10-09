from app import db

class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), nullable=False)
  year = db.Column(db.Integer)

  def __repr__(self):
    return '<Movie %r>' % self.title
