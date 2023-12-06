from django.db import models
from django.contrib.auth.models import User
import uuid


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
