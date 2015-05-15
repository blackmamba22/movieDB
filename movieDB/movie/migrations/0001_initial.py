# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(help_text=b'First Name', max_length=128)),
                ('last_name', models.CharField(help_text=b'Last Name', max_length=128)),
                ('full_name', models.CharField(help_text=b'Full Name', max_length=128)),
                ('gender', models.CharField(help_text=b'Male or Female', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('age', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'movie title', max_length=128)),
                ('year', models.IntegerField(help_text=b'release year')),
                ('length', models.IntegerField(help_text=b'length (in minutes)')),
                ('raw_name', models.CharField(max_length=128, editable=False)),
                ('file_path', models.CharField(max_length=255, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(to='movie.MovieGenre'),
            preserve_default=True,
        ),
    ]
