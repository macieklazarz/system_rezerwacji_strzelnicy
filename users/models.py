from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    nr_telefonu = models.CharField(max_length=9)

    def __str__(self):
        return f"Profil użytkownika {self.user.username}"


# Create your models here.
