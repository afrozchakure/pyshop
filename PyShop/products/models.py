from django.db import models


class Product(models.Model):  # It inherits from Model object
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length = 2083)  # standard max length of urls




