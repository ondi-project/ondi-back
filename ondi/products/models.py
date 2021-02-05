from django.db import models
from user.models import *
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    content = models.TextField(blank=True)
    image = models.ImageField(null=True)
    negotiable = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_seller')
    view_count = models.IntegerField(default=0)
    # live = BooleanField()
    # like_count
