from django.contrib import admin
from models import Movie, MovieGenre, Actor

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'length', 'tv_show','release_date')
    search_fields = ('title', )
    list_filter = ('release_date',)
    ordering = ('title',)
    filter_horizontal = ('actors',)

class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'age')
    search_fields = ('first_name', 'last_name')


admin.site.register(MovieGenre, MovieGenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)