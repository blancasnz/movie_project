from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://localhost:5432/blanca_movies'
db = SQLAlchemy(app)




