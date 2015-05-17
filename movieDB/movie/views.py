from django.shortcuts import render
from django.http import HttpResponse
from models import Movie
from forms import MovieSearchForm

# Create your views here.

def hello(request):
    import datetime

    now = str(datetime.datetime.now())
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index3(request):
    print request.GET
    return render(request, 'movie/index.html', {})


def index(request):

    if 'moviequery' in request.GET and request.GET['moviequery']:
        moviequery = request.GET['moviequery']

        movies = Movie.objects.filter(title__icontains=moviequery)
        context_dict = {'movies' : movies}

        return render(request, 'movie/index.html', context_dict)
    else:
        print request.POST
        return render(request, 'movie/index.html', {})



