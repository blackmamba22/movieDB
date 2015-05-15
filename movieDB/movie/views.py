from django.shortcuts import render
from django.http import HttpResponse
from models import Movie

# Create your views here.

def hello(request):
    import datetime

    now = str(datetime.datetime.now())
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    return render(request, 'movie/index.html', {})
