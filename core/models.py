from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tor(models.Model):
	nazwa = models.CharField(max_length=100)
	opis = models.TextField()
	is_active = models.BooleanField(default=True)


	def __str__(self):
		return self.nazwa

# Create your models here.
