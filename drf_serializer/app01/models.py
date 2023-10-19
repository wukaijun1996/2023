from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.CharField(max_length=32)
    publish = models.CharField(max_length=32)
