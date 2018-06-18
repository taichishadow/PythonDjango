from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=20)

class User(models.Model):
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    photo = models.CharField(max_length=20, blank=True)
    role = models.ForeignKey(Role);