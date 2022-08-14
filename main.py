from flask import Flask, jsonify

from utils import get_by_title, get_by_years, get_by_audience, get_by_genre

app = Flask(__name__)


@app.route("/movie/<title>")
def movie_by_title(title):
    """
    Страничка одного фильма
    """
    movie = get_by_title(title)
    return jsonify(movie)


@app.route("/movie/<int:year_1>/to/<int:year_2>")
def movies_by_years(year_1, year_2):
    """
    Страничка фильмов по дате выхода
    """
    movies = get_by_years(year_1, year_2)
    return jsonify(movies)


@app.route("/rating/<audience>")
def movies_by_audience(audience):
    """
    Страничка фильмов для выбранной аудитории
    """
    movies = get_by_audience(audience)
    return jsonify(movies)


@app.route("/genre/<genre>")
def movies_by_genre(genre):
    """
    Страничка фильмов выбранного жанра
    """
    movies = get_by_genre(genre)
    return jsonify(movies)


if __name__ == '__main__':
    app.run()
