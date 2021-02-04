from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator

# Create your models here.
class User(AbstractUser):
   phone = models.CharField(max_length=11, validators=[MinLengthValidator(11)])

class Score(models.Model):
  class Meta:
    unique_together = ('from_user', 'to_user',)

  from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_from_user')
  to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_to_user')
  score = models.IntegerField(
    validators=[
      MaxValueValidator(100),
      MinValueValidator(1)
    ]
  )

class Report(models.Model):
  class Meta:
    unique_together = ('from_user', 'to_user',)
  from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_from_user')
  to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_to_user')
  content = models.TextField(max_length=255)

class Favorite(models.Model):
  class Meta:
    unique_together = ('from_user',)
  from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_from_user')
  # item

class Notification(models.Model):
  to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_to_user')
  message = models.TextField()

'''
class Like(models.Model):
    user
    item

class Purchased(models.Model):
    user
    item
'''
