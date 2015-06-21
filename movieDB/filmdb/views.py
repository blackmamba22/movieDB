from django.shortcuts import render
from django.http import HttpResponse

import string
import os
import subprocess


from models import Film
# Create your views here.

def index4(request):
    import datetime

    now = str(datetime.datetime.now())
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def index(request):
    if 'moviequery' in request.GET and request.GET['moviequery']:
        moviequery = request.GET['moviequery']

        movies = Film.objects.filter(title__icontains=moviequery)
        context_dict = {'movies': movies}

        return render(request, 'filmdb/index.html', context_dict)
    else:
        #print request.POST
        return render(request, 'filmdb/index.html', {})


def film_page(request, film_slug):
    context_dict = {}

    try:
        film = Film.objects.get(slug=film_slug)
        context_dict['film'] = film

        if film.file_path == 'n/a':
            context_dict['error'] = 'Video file cannot be found'
    except Film.DoesNotExist:
        pass

    return render(request, 'filmdb/film.html', context_dict)


def browse_page(request):

    # List of alphabets from A - Z
    alphabets = [letter for letter in string.ascii_uppercase]
    context_dict = {}#{let: None for let in alphabets}

    f = []

    try:
        for letter in alphabets:
            films = Film.objects.filter(title__startswith=letter)
            #context_dict[letter] = films
            f.append({letter:films})

        context_dict['filled'] = 'filled'
        context_dict['films'] = f

    except Film.DoesNotExist:
        pass

    context_dict['alpha'] = alphabets

    return render(request, 'filmdb/browse.html', context_dict)


def play_film(request, film_slug):

    context_dict = {}


    film = Film.objects.get(slug=film_slug)

    if film and film.file_path != 'n/a':
        cmds = ["vlc", film.file_path]
        subprocess.call(cmds)       # open vlc play with the file_path
        context_dict['film'] = film


    return render(request, 'filmdb/film.html', context_dict)





