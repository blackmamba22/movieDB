from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="index"),
    url(r'^film/(?P<film_slug>[\w\-]+)/$', views.film_page, name="film_page"),

)