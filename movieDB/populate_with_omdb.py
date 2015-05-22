import omdb

import unicodedata
import json
import re
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieDB.settings')

import django
django.setup()

from movie.models import Film, MovieGenre, Actor, Director, Country

movie_list = ['Breaking Bad', 'Seinfeld', 'The Naked Gun', 'Swordfish', '2 Fast 2 Furious']

#print omdb.get(title='True Grit', year=1969, fullplot=True, tomatoes=True)
#movie = omdb.title('Breaking Bad')
#scatman = omdb.get(title='Seinfeld')


def populate_films(films=[]):

    for f in films:
        film = omdb.get(title=f)

        title = film.get('title')
        year = film.get('year')
        type = film.get('type')
        actors = film.get('actor')
        awards = film.get('awards')
        country = film.get('country')
        directors = film.get('director')
        genre = film.get('genre')
        language = film.get('language')
        plot = film.get('plot')
        poster = film.get('poster')
        released = film.get('released')
        runtime = film.get('runtime')
        imdb_id = film.get('imdb_id')

        # Adding models to DB

        film_model = Film.objects.get_or_create(title=title)[0]
        film_model.year = year
        film_model.type = type
        film_model.plot = plot
        film_model.poster = poster
        film_model.released = released
        film_model.runtime = runtime
        film_model.imdb_id = imdb_id
        film_model.award = awards

        # Strings to list
        if directors != 'N/A':
            director_name = (unicodedata.normalize('NFKD', directors).encode('ascii', 'ignore'))
            add_director(director_name)
            film_model.director = director_name

        if genre != 'N/A':
            g = (unicodedata.normalize('NFKD', genre).encode('ascii', 'ignore')).split(",")
            print g
            film_model.genre = MovieGenre(g[0])
            for i in g:
                add_genre(i)


        if country != 'N/A':
            c = (unicodedata.normalize('NFKD', country).encode('ascii', 'ignore')).split(",")
            print c
            #film_model.country.add(c[0])
            for i in c:
                add_country(i)


        film_model.save()


def add_director(dname):
    d = Director.objects.get_or_create(name=dname)[0]
    d.save()


def add_genre(gen):
    g = MovieGenre.objects.get_or_create(name=gen)[0]
    g.save()


def add_country(name):
    c = Country.objects.get_or_create(country_name=name)[0]
    c.save()





if __name__ == '__main__':
   # populate_films(films=['Breaking Bad', 'Seinfeld', 'The Naked Gun', 'Swordfish', '2 Fast 2 Furious'])
    s = omdb.get(title='True Grit', year=1969, fullplot=True, tomatoes=True)
    print json.dump(s.get('title'), separators=('', ':'), ensure_ascii=True)
