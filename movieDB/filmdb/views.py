from django.shortcuts import render
from django.http import HttpResponse


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


"""

def index3(request):

    if 'moviequery' in request.GET and request.GET['moviequery']:
        moviequery = request.GET['moviequery']

        movies = Film.objects.filter(title__icontains=moviequery)
        context_dict = {'movies': movies}

        return render(request, 'movie/index.html', context_dict)
    else:
        #print request.POST
        return render(request, 'movie/index.html', {})"""