import re
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieDB.settings')

import django
django.setup()

from movie.models import Movie, MovieGenre

def populate():

    movie_source = '/home/gawaine/Videos/moviedb'

    for root, dirs, files in os.walk(movie_source):

        for filename in files:
            fullname = os.path.join(root, filename)

            if is_movie_extension(filename):
                #print "Complete name: ", fullname, \
                #print "File: ", filename,"\n"
                add_movie(vidname=filename, filepath=fullname)

def populate_genres():

    genres = ['Action Films', 'Adventure Films', 'Comedy Films', 'Crime & Gangster Films', 'Drama Films', 'Epics/Historical Films',
              'Horror Films', 'Musicals (Dance) Films', 'Science Fiction Films', 'War (Anti-War) Films', 'Westerns']

    for g in genres:
        print "Adding film genre: ", g
        add_movie_genre(g)

def is_movie_extension(filename, movie_extensions=['avi', 'dat', 'mp4', 'mkv', 'mov', 'mpg', 'rmvb','vob']):

    for ext in movie_extensions:

        pattern =  r"(.*)\." + ext + r"$"
        extension_object = re.search(pattern, filename, re.I)

        if extension_object:
            return True

    return False


def add_movie(vidname, filepath):
    movie = Movie.objects.get_or_create(raw_name=vidname)[0]
    movie.file_path = filepath
    movie.title = vidname
    movie.save()

    return movie


def add_movie_genre(genre):
    mg = MovieGenre.objects.get_or_create(name=genre)[0]
    mg.save()

    return mg



if __name__ == '__main__':
    populate_genres()
    populate()


