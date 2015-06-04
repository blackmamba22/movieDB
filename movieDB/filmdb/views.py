from django.shortcuts import render
from django.http import HttpResponse

import string

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




