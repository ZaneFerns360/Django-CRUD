from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date published")
    address = models.CharField(max_length=300)
    type = models.CharField(max_length=30)
    timings = models.TimeField()
    likes = models.BigIntegerField()
    contact_info = models.CharField(max_length=40)
