from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class Director(models.Model):
    director_name = models.CharField(max_length=30)
    director_surname = models.CharField(max_length=30)
    director_age = models.IntegerField()

    def __str__(self):
        return self.director_name + " " + self.director_surname


class Movie(models.Model):
    dirco = models.ForeignKey(Director,on_delete=CASCADE)
    film_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.film_name