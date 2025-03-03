from django.db import models
from django.contrib.auth.models import User

class CustomManager(models.Manager):
    def mobile_list(self):
        return self.filter(category__exact="Mobile")
    def cloth_list(self):
        return self.filter(category__exact="Cloths")
    def shoes_list(self):
        return self.filter(category__exact="Shoes")

    def electronics_list(self):
        return self.filter(category__exact="Electronics")

    def pricerange(self,r1,r2):
        return self.filter(price__range=(r1,r2))

    


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
    objects=models.Manager()
    productmanager=CustomManager()


class Cart(models.Model):
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)


class Orders(models.Model):
    orderid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)

class Address(models.Model):
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    mobile= models.PositiveIntegerField()
    address=models.TextField()
    pincode=models.PositiveIntegerField()

class Payment(models.Model):
    receiptid=models.PositiveIntegerField()
    orderid=models.ForeignKey(Orders,on_delete=models.SET_NULL,null=True)
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    totalprice=models.FloatField()

    