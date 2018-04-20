from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField()
    code = models.CharField(max_length=20)

class Player(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    birthdate = models.DateField()
    age = models.IntegerField()
    rut = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    height = models.FloatField()
    weight = models.IntegerField()
    photo = models.ImageField()
    position = models.CharField(
            max_length=2,
            choices=(
                    ('BA', 'Base'),
                    ('ES', 'Escolta'),
                    ('AL', 'Alero'),
                    ('AP', 'AlaPivot'),
                    ('PI', 'Pivot'),
                    ),
            default='BA'
            )
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Couch(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    age = models.IntegerField()
    rut = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)

class Match(models.Model):
    name = models.CharField(max_length=100)
