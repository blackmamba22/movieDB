# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20150512_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(help_text=b'First Name', max_length=128)),
                ('last_name', models.CharField(help_text=b'Last Name', max_length=128)),
                ('full_name', models.CharField(help_text=b'Full Name', max_length=128)),
                ('gender', models.CharField(help_text=b'Male or Female', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('age', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_name', models.CharField(default=b'Pangea', help_text=b'Country Name', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Blank', help_text=b'Director Name', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Blank', help_text=b'film title', max_length=128)),
                ('year', models.CharField(help_text=b'release year', max_length=15, null=True, blank=True)),
                ('type', models.CharField(default=b'movie', help_text=b'series, movie', max_length=20)),
                ('award', models.CharField(default=b'Blank', max_length=128, null=True, help_text=b'film awards')),
                ('plot', models.TextField(help_text=b'Film plot', max_length=256, null=True, blank=True)),
                ('poster', models.CharField(help_text=b'link to poster image', max_length=256, null=True, blank=True)),
                ('released', models.CharField(default=b'Blank', help_text=b'release date', max_length=128)),
                ('runtime', models.CharField(default=b'Blank', help_text=b'film length', max_length=15)),
                ('imdb_id', models.CharField(default=1, max_length=15, null=True, blank=True)),
                ('rated', models.CharField(default=1, max_length=15, null=True, blank=True)),
                ('actor', models.ManyToManyField(to='movie.Actor', verbose_name=b'Actor/Actress', blank=True)),
                ('country', models.ManyToManyField(default=1, to='movie.Country', blank=True)),
                ('director', models.ForeignKey(default=1, to='movie.Director')),
                ('genre', models.ForeignKey(default=1, to='movie.MovieGenre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_name', models.CharField(default=b'Blank', help_text=b'Language', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Actors',
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.ManyToManyField(to='movie.Language'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movie.Actor', verbose_name=b'Actor/Actress', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='date_entered',
            field=models.DateTimeField(default=datetime.date(2015, 5, 26)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 26, 17, 43, 4, 256949)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='tv_show',
            field=models.BooleanField(default=False, help_text=b'Is it a TV Show or not?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='file_path',
            field=models.CharField(max_length=255, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(default=1, to='movie.MovieGenre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.IntegerField(default=65, help_text=b'length (in minutes)', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='raw_name',
            field=models.CharField(max_length=128, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(default=b'FakeTitle', help_text=b'movie title', max_length=128, blank=True),
        ),
    ]
