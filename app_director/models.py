from django.db import models

# Create your models here.

class Director(models.Model):
    director_name = models.CharField(max_length=30)
    director_surname = models.CharField(max_length=30)
    director_age = models.IntegerField()

    def __str__(self):
        return self.director_name + " " + self.director_surname