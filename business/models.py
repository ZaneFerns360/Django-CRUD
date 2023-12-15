from django.db import models
from django.contrib.auth.models import User
import uuid


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)


class Images(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.CharField(max_length=500)


class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date published")
    address = models.CharField(max_length=300)
    type = models.CharField(max_length=30)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    likes = models.BigIntegerField()
    contact_info = models.CharField(max_length=40)
    image = models.CharField(max_length=500)
    items = models.ManyToManyField(Item, blank=True)  # allow no items
    other_images = models.ManyToManyField(Images)
