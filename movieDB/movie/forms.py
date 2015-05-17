from django import forms
from models import Movie


class MovieSearchForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Search for movie title')

    class Meta:
        model = Movie
        fields = ('title',)
