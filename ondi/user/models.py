from django.apps import apps
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    image = models.ImageField(null=True)

class Score(models.Model):
    class Meta:
        unique_together = ('from_user', 'to_user',)

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_to_user')
    score = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    comment = models.TextField()

class Report(models.Model):
    class Meta:
        unique_together = ('from_user', 'to_user',)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_to_user')
    content = models.TextField(max_length=255)

class Notification(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_to_user')
    message = models.TextField()

class Favorite(models.Model):
    class Meta:
        unique_together = ('from_user', 'product',)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_from_user')
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE, related_name='%(class)s_product')

class Like(models.Model):
    class Meta:
        unique_together = ('from_user', 'product',)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_from_user')
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE, related_name='%(class)s_product')

class Sold(models.Model):
    class Meta:
        unique_together = ('from_user', 'product',)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_from_user')
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE, related_name='%(class)s_product')
    price = models.IntegerField()
