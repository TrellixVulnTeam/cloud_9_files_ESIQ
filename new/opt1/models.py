from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser,models.Model):
    gender = models.CharField(max_length=100)
