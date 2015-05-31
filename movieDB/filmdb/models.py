from django.db import models

# Create your models here.

class Language(models.Model):
    language_name = models.CharField(max_length=128, default='Blank', help_text='Language')

    def __unicode__(self):
        return self.language_name


class Country(models.Model):
    country_name = models.CharField(max_length=128, default='Pangea', help_text='Country Name')
    language = models.ManyToManyField(Language, blank=True)

    def __unicode__(self):
        return self.country_name


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Director(models.Model):
    full_name = models.CharField(max_length=128, default='Blank', help_text='Director Name')

    def __unicode__(self):
        return self.full_name


class Writer(models.Model):
    full_name = models.CharField(max_length=128, default='Blank', help_text='Writer Name')

    def __unicode__(self):
        return self.full_name


class Actor(models.Model):
    full_name = models.CharField(max_length=128, help_text='Full Name')
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), null=True,help_text='Male or Female')
    age = models.IntegerField(default=1, null=True)

    def __unicode__(self):
        return self.full_name


class Film(models.Model):
    title = models.CharField(max_length=128, default='Blank', help_text='film title')
    year = models.CharField(max_length=15, help_text='release year', blank=True, null=True)
    rated = models.CharField(max_length=15, default=1, null=True, blank=True)
    released = models.CharField(max_length=128, default='Blank', help_text='release date')
    runtime = models.CharField(max_length=15, default='Blank', help_text='film length')
    genre = models.ManyToManyField(Genre, default=1, blank=True)
    director = models.ManyToManyField(Director, default=1, blank=True)
    type = models.CharField(max_length=20, default='movie', help_text='series, movie etc')
    actor = models.ManyToManyField(Actor, blank=True, verbose_name='Actor/Actress')
    award = models.CharField(max_length=128, default='Blank', null=True,help_text='film awards')
    country = models.ManyToManyField(Country, default=1, blank=True)
    language = models.ManyToManyField(Language)
    plot = models.TextField(max_length=256, help_text="Film plot", null=True, blank=True)
    poster = models.URLField(max_length=256, help_text='link to poster image', blank=True, null=True)
    imdb_id = models.CharField(max_length=15, default=1, null=True, blank=True)
    imdb_rating = models.CharField(max_length=15, null=True, blank=True)
    meta_score = models.CharField(max_length=10, null=True,blank=True)

    def __unicode__(self):
        return self.title + self.year