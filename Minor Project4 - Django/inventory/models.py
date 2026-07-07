from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name
