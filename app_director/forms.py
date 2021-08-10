from django.forms import ModelForm, fields
from .models import Director
from django import forms


class YonetmenForm(forms.ModelForm):
    class Meta:
        model = Director
        fields =[
            'director_name',
            'director_surname',
            'director_age',
        ]