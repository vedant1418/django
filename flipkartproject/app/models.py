from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.IntegerField(primary_key=True)
    productname = models.CharField(max_length=60)
    type = (
        ("Mobile", "Mobile"),
        ("Cloths", "Cloths"),
        ("Shoes", "Shoes"),
        ("Electronics", "Electronics"),
    )
    category = models.CharField(max_length=50, choices=type)
    description = models.TextField()
    price = models.FloatField()
    images = models.ImageField(upload_to="photos")


class Cart(models.Model):
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)


class Orders(models.Model):
    orderid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)
