from django.db import models

# Create your models here.


class MovieGenre(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Movie(models.Model):
    title = models.CharField(max_length=128, help_text='movie title')
    year = models.IntegerField(help_text='release year')
    length = models.IntegerField(help_text='length (in minutes)')
    genre = models.ForeignKey(MovieGenre)
    raw_name = models.CharField(max_length=128, editable=False)
    file_path = models.CharField(max_length=255, editable=False)


class Actors(models.Model):
    first_name = models.CharField(max_length=128, help_text='First Name')
    last_name = models.CharField(max_length=128, help_text='Last Name')
    full_name = models.CharField(max_length=128, help_text='Full Name')
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), help_text='Male or Female')
    age = models.IntegerField()

