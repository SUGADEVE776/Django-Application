from django.db import models

# Create your models here.


class Laptop(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    touch_screen = models.BooleanField()
    
    class Meta:
        db_table = 'Laptop'
        ordering = ("price",)