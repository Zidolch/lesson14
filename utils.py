import sqlite3

DB_PATH = "project/netflix.db"


def get_query_result(query):
    """
    Делает запрос к базе данных
    """
    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(query).fetchall()
        return result


def get_by_title(title):
    """
    Возвращает информацию о фильме по названию
    """
    query = f"""
        SELECT title, country, release_year, listed_in as genre, description
        FROM netflix
        WHERE title = {title}
        ORDER BY release_year
        LIMIT 1
    """
    query_result = get_query_result(query)
    result = []
    for row in query_result:
        result.append(dict(row))
    return result


def get_by_years(year_1, year_2):
    """
    Возвращает информацию о фильмах, вышедших в указанных годах
    """
    query = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {year_1} AND {year_2}
        ORDER BY release_year
        LIMIT 100            
    """
    query_result = get_query_result(query)
    result = []
    for row in query_result:
        result.append(dict(row))
    return result


def get_by_audience(audience):
    """
    Возвращает информацию о фильмах с указанным рейтингом
    """
    ratings = {
        "children": "G",
        "family": ("G", "PG", "PG-13"),
        "adult": ("R", "NC-17")
    }
    query = f"""
        SELECT title, rating, description
        FROM netflix
        WHERE rating IN {ratings[audience]}
        LIMIT 100
    """
    query_result = get_query_result(query)
    result = []
    for row in query_result:
        result.append(dict(row))
    return result


def get_by_genre(genre):
    """
    Возвращает информацию о новых фильмах указанного жанра
    """
    query = f"""
        SELECT title, description
        FROM netflix
        WHERE listed_in LIKE '%{genre}%'
        ORDER BY release_year DESC
        LIMIT 10
    """
    query_result = get_query_result(query)
    result = []
    for row in query_result:
        result.append(dict(row))
    return result


def get_colleagues(actor_1, actor_2):
    """
    Возвращает список актеров, которые более двух раз
    снимались с двумя указанными актерами
    """
    query = f"""
        SELECT *
        FROM netflix
        WHERE "cast" LIKE '%{actor_1}%'
        AND "cast" LIKE '%{actor_1}%'
        limit 100

    """
    query_result = get_query_result(query)
    colleagues = []
    names_dict = {}

    for row in query_result:
        names = set(dict(row).get('cast').split(', ')) - {actor_1, actor_2}
        for name in names:
            names_dict[name.strip()] = names_dict.get(name.strip(), 0) + 1
    for key, value in names_dict.items():
        if value > 2:
            colleagues.append(key)

    return colleagues


def get_by_type_year_genre(film_type, year, genre):
    """
    Возвращает информацию о фильмах с указанным типом, годом выпуска и жанром
    """
    query = f"""
        SELECT title, description
        FROM netflix
        WHERE type = '{film_type}'
        AND release_year = {year}
        AND listed_in LIKE '%{genre}%'
        LIMIT 10
    """
    query_result = get_query_result(query)
    result = []
    for row in query_result:
        result.append(dict(row))
    return result
