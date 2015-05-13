from django.db import models

# Create your models here.


class MovieGenre(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Movie(models.Model):
    title = models.CharField(max_length=128, help_text='movie title', null=True)
    year = models.IntegerField(help_text='release year', null=True)
    length = models.IntegerField(help_text='length (in minutes)', null=True)
    genre = models.ForeignKey(MovieGenre, null=True)
    raw_name = models.CharField(max_length=128, editable=False, null=True)
    file_path = models.CharField(max_length=255, editable=False, null=True)

    def __unicode__(self):
        return self.title + self.year


class Actors(models.Model):
    first_name = models.CharField(max_length=128, help_text='First Name')
    last_name = models.CharField(max_length=128, help_text='Last Name')
    full_name = models.CharField(max_length=128, help_text='Full Name')
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), help_text='Male or Female')
    age = models.IntegerField()


