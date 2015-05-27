import omdb
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieDB.settings')

import django
django.setup()


from movie.models import Film, MovieGenre, Actor, Director, Country

movie_list = ['Breaking Bad', 'Seinfeld', 'The Naked Gun', 'Swordfish', '2 Fast 2 Furious']


def populate_films(films=['The Transporter']):

    for f in films:
        film = omdb.get(title=f)

        for i in film:

            film[i] = film[i].encode("utf-8").strip()
            print i, ": ", film[i]


        title = film.get('title')
        year = film.get('year')
        type_film = film.get('type')
        actors = film.get('actors')
        awards = film.get('awards')
        country = film.get('country')
        directors = film.get('director')
        genre = film.get('genre')
        language_film = film.get('language')
        plot = film.get('plot')
        poster = film.get('poster')
        released = film.get('released')
        runtime = film.get('runtime')
        imdb_id = film.get('imdb_id')

        # Adding models to DB

        film_model = Film.objects.get_or_create(title=title)[0]
        film_model.year = year
        film_model.type = type_film
        film_model.plot = plot
        film_model.poster = poster
        film_model.released = released
        film_model.runtime = runtime
        film_model.imdb_id = imdb_id
        film_model.award = awards
        film_model.rated = film.get("rated")

        # Strings to list
        if directors != 'N/A':
            a = actors.strip().split(",")

            if isinstance(a, tuple) or isinstance(a, list):
                for i in a:
                    tmp = Actor.objects.get_or_create(full_name=i)[0]
                    film_model.actor.add(Actor.objects.get(pk=tmp.id))
            else:
                tmp = Actor.objects.get_or_create(full_name=actors)[0]
                film_model.actor.add(Actor.objects.get(pk=tmp.id))

        if genre != 'N/A':
            g = genre.strip().split(",")

            if isinstance(g, tuple) or isinstance(g, list):
                for i in g:
                    tmp = MovieGenre.objects.get_or_create(name=i)[0]
                    film_model.genre = MovieGenre.objects.get(pk=tmp.id)
            else:
                tmp = MovieGenre.objects.get_or_create(name=genre)[0]
                film_model.genre = MovieGenre.objects.get(pk=tmp.id)

        if country != 'N/A':
            c = country.strip().split(",")

            if isinstance(c, tuple) or isinstance(c, list):
                for i in c:
                    tmp = Country.objects.get_or_create(country_name=i)[0]
                    film_model.country.add(Country.objects.get(pk=tmp.id))
            else:
                tmp = Country.objects.get_or_create(country_name=country)[0]
                film_model.country.add(Country.objects.get(pk=tmp.id))

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
    #add_director('John Singleton')
    #add_country('USA')
    #add_genre('Comedy')
    populate_films(films=['Breaking Bad', 'Seinfeld', 'The Naked Gun', 'Swordfish', '2 Fast 2 Furious', 'Fast', 'Step Brothers'])
    #s = omdb.get(title='True Grit', year=1969, fullplot=True, tomatoes=True)



