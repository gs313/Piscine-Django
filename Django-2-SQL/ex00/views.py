from django.http import HttpResponse
import psycopg2


def init(request):
    try:
        connection = psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='localhost',
            port='5432'
        )

        cursor = connection.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS ex00_movies (
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb INTEGER PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """

        cursor.execute(query)

        connection.commit()

        cursor.close()
        connection.close()

        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(e)
