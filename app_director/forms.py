from django.forms import ModelForm, fields
from .models import Director,Movie
from django import forms


class YonetmenForm(forms.ModelForm):
    class Meta:
        model = Director
        fields =[
            'director_name',
            'director_surname',
            'director_age',
        ]


class FilmForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'dirco',
            'film_name',
            'country',
        ]

class FilmFormNoDirector (forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'film_name',
            'country',
        ]