from django.contrib import admin
from models import Genre, Film, Actor

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'age')
    search_fields = ('full_name',)


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'released', 'type', 'runtime','imdb_rating')
    search_fields = ('title',)
    list_filter = ('year',)
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Film, FilmAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)