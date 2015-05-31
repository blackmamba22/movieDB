from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    import datetime

    now = str(datetime.datetime.now())
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)