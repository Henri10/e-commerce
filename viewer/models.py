from django.contrib.auth.models import User
from django.db import models
import uuid

from django.db.models import DO_NOTHING


class Products(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Smartphone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.ForeignKey(Products, on_delete=DO_NOTHING)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    image_of_product = models.ImageField()
    like = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
