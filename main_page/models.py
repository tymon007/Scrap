from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=200, help_text="Type your username here")
    email = models.EmailField(help_text="Type your email here")
    password = models.CharField(max_length=200, help_text="Type your password here")
    salt = models.CharField(max_length=200, help_text="Salt for password", default="")

    def __str__(self):
        return '%s' % self.username

class KodOdpadu(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    opis = models.TextField(help_text="It is text describing user's problem here")

class Rekord(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa_metalu = models.TextField(help_text="It is text describing user's problem here")
    content = models.TextField(help_text="It is text describing user's problem here")
    waga = models.IntegerField(help_text="It is numeric representation of waga")
    kod_odpadu = models.ForeignKey(KodOdpadu, on_delete=models.CASCADE)
