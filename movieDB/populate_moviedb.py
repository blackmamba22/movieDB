import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieDB.settings')
import re

import django
django.setup()


from movie.models import Movie, MovieGenre

def populate():

    movie_source = '/home/gawaine/Videos/moviedb'

    for root, dirs, files in os.walk(movie_source):

        for filename in files:
            path = os.path.join(root, filename)
            film_title = os.path.basename(filename)

            if is_movie_extension(filename):
                #print "Complete name: ", fullname, \
                print "Adding Film: ", filename
                add_movie(vidname=filename, filepath=path)


def is_movie_extension(filename, movie_extensions=['avi', 'dat', 'mp4', 'mkv', 'mov', 'mpg', 'rmvb','vob']):

    for ext in movie_extensions:

        pattern =  r"(.*)\." + ext + r"$"
        extension_object = re.search(pattern, filename, re.I)

        if extension_object:
            return True

    return False


def add_from_folder(folder_name):

    for root, dirs, files in os.walk(folder_name):

        for filename in files:
            path = os.path.join(root, filename)
            film_title = os.path.basename(filename)

            if is_movie_extension(filename):
                #print "Complete name: ", fullname, \

                add_film(vidname=filename, filepath=path)



if __name__ == '__main__':

    populate()


