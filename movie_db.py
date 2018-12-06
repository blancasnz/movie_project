import requests
import json
import os


class Movie(object):

    def __init__(self, movie_id, title, release_date):
        self.movie_id = movie_id
        self.title = title
        self.release_date = release_date

    def to_dictionary(self):
        movie_dictionary = {
            'movie_id': self.movie_id,
            'title': self.title,
            'release_date': self.release_date
        }

        return movie_dictionary

    def __repr__(self):
        return '<Movie %r %r>' % (self.title, self.release_date)


def search(query):
    payload = {
        'api_key': os.environ.get('MOVIE_DB_API_KEY'),
        'query': query
    }

    response = requests.get(
        'https://api.themoviedb.org/3/search/multi', params=payload)

    output = json.loads(response.text)
    movies = []
    for film in output['results']:
        movies.append(Movie(film['id'], film['title'], film['release_date']))

    return movies


output = search('die hard')
print(output[:5])
