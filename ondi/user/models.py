from django.db import models

# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=200)
