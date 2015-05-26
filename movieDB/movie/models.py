from django.db import models
from datetime import datetime, date
# Create your models here.


class MovieGenre(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=128, help_text='First Name')
    last_name = models.CharField(max_length=128, help_text='Last Name')
    full_name = models.CharField(max_length=128, help_text='Full Name')
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), help_text='Male or Female')
    age = models.IntegerField(default=1)

    def __unicode__(self):
        return self.first_name + self.last_name


class Movie(models.Model):
    title = models.CharField(max_length=128, default='FakeTitle',help_text='movie title', blank=True)
    length = models.IntegerField(default=65, help_text='length (in minutes)', blank=True)
    genre = models.ForeignKey(MovieGenre, default=1)
    tv_show = models.BooleanField(default=False, help_text='Is it a TV Show or not?', blank=True)
    raw_name = models.CharField(max_length=128, editable=False, blank=True)
    file_path = models.CharField(max_length=255, editable=False, blank=True)
    actors = models.ManyToManyField(Actor, blank=True, verbose_name='Actor/Actress')

    import datetime
    date_entered = models.DateTimeField(default=datetime.date.today())
    release_date = models.DateField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.title + str(self.release_date)


class Language(models.Model):
    language_name = models.CharField(max_length=128, default='Blank', help_text='Language')

    def __unicode__(self):
        return self.language_name


class Country(models.Model):
    country_name = models.CharField(max_length=128, default='Pangea', help_text='Country Name')

    def __unicode__(self):
        return self.country_name


class Director(models.Model):
    name = models.CharField(max_length=128, default='Blank', help_text='Director Name')

    def __unicode__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=128, default='Blank', help_text='film title')
    year = models.CharField(max_length=15, help_text='release year', blank=True, null=True)
    type = models.CharField(max_length=20, default='movie', help_text='series, movie')
    actor = models.ManyToManyField(Actor, blank=True, verbose_name='Actor/Actress')
    award = models.CharField(max_length=128, default='Blank', null=True,help_text='film awards')
    country = models.ManyToManyField(Country, default=1, blank=True)
    director = models.ForeignKey(Director, default=1)
    genre = models.ForeignKey(MovieGenre, default=1)
    language = models.ManyToManyField(Language)
    plot = models.TextField(max_length=256, help_text="Film plot", null=True, blank=True)
    poster = models.CharField(max_length=256, help_text='link to poster image', blank=True, null=True)
    released = models.CharField(max_length=128, default='Blank', help_text='release date')
    runtime = models.CharField(max_length=15, default='Blank', help_text='film length')
    imdb_id = models.CharField(max_length=15, default=1, null=True, blank=True)



