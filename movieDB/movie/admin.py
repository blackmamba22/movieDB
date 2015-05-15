from django.contrib import admin
from models import Movie, MovieGenre, Actor

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'length', 'tv_show','release_date')
    search_fields = ('title',)

class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(MovieGenre, MovieGenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)