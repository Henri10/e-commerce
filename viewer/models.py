from django.contrib.auth.models import User
from django.db import models
import uuid

from django.db.models import DO_NOTHING


class Products(models.Model):
    object = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Smartphone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    products = models.ForeignKey(Products, on_delete=DO_NOTHING)
    name_product = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    image_of_product = models.ImageField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_product
