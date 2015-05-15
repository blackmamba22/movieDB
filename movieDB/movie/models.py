from django.db import models

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





