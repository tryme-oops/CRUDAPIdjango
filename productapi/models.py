from django.db import models

# Create your models here.

class product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=200)
    price = models.IntegerField()
    product_image = models.ImageField(null=True, blank = True)
