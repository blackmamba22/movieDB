import omdb
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieDB.settings')

import django
django.setup()

from filmdb.models import *


def add_film(film_list=[]):
    """"
    Takes a list of tuples ex. films = [ (film_title, file_path_for_film) ]
    """
    #
    for film in film_list:
        film_json_obj = omdb.get(title=film[0], fullplot=True, tomatoes=True)
        #print film_json_obj

        # Check if film was actually received, if not skip to next film
        if film_json_obj.get('response') is None:
            print "FAILED. Was not able to retrieve film for via omdb api. Please check the title."
            continue

        # Convert all attributes for a film to unicode.
        for att in film_json_obj:
            film_json_obj[att] = film_json_obj[att].encode("utf-8").strip()

        filmmodel = Film.objects.get_or_create(title=film_json_obj.get('title'))[0]
        filmmodel.year = film_json_obj.get('year')
        filmmodel.rated = film_json_obj.get('rated')
        filmmodel.released = film_json_obj.get('released')
        filmmodel.runtime = film_json_obj.get('runtime')
        filmmodel.type = film_json_obj.get('type')
        filmmodel.award = film_json_obj.get('award')
        filmmodel.plot = film_json_obj.get('plot')
        filmmodel.poster = film_json_obj.get('poster')
        filmmodel.imdb_id = film_json_obj.get('imdb_id')
        filmmodel.imdb_rating = film_json_obj.get('imdb_rating')
        filmmodel.meta_score = film_json_obj.get('meta_score')
        filmmodel.file_path = film[1]

        for l in film_json_obj.get('language').strip().split(","):
            new_language = Language.objects.get_or_create(language_name=l)[0]
            filmmodel.language.add(new_language)

        for g in film_json_obj.get('genre').strip().split(","):
            new_genre = Genre.objects.get_or_create(name=g)[0]
            filmmodel.genre.add(new_genre)

        for c in film_json_obj.get('country').strip().split(","):
            new_country = Country.objects.get_or_create(country_name=c)[0]
            filmmodel.country.add(new_country)

        for a in film_json_obj.get('actors').strip().split(","):
            new_actor = Actor.objects.get_or_create(full_name=a)[0]
            filmmodel.actor.add(new_actor)

        for d in film_json_obj.get('director').strip().split(","):
            new_director = Director.objects.get_or_create(full_name=d)[0]
            filmmodel.director.add(new_director)

        for w in film_json_obj.get('writer').strip().split(","):
            new_writer = Writer.objects.get_or_create(full_name=w)[0]
            filmmodel.writer.add(new_writer)

        filmmodel.save()
        print "Adding film....", filmmodel.title, filmmodel.year






if __name__ == '__main__':

    #populate_films(films=['Breaking Bad', 'Seinfeld', 'The Naked Gun', 'Swordfish', '2 Fast 2 Furious', 'Fast', 'Step Brothers'])
    #s = omdb.get(title='Spy Hard', fullplot=True, tomatoes=True)
    #print s

    films = [('Spy Hard', 'n/a'), ('The Naked Gun', 'n/a'), ('Seinfeld', 'n/a')]
    add_film(films)



