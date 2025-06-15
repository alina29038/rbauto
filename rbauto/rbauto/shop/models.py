from django.db import models
from django.contrib.auth.models import User
from .enums import ORDER_TYPE, ORDER_STATUS

# Create your models here.
class Category(models.Model):
    title = models.CharField()
    image = models.FileField(upload_to="images/categories/")

class Manufacturer(models.Model):
    title = models.CharField()
    logo = models.FileField(upload_to="images/manufacturers/", null=True)

class Subcategory(models.Model):
    title = models.CharField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product(models.Model):
    title = models.CharField()
    description = models.TextField()
    preview = models.FileField(upload_to="images/products/")
    price = models.CharField()
    is_available = models.BooleanField()
    details = models.JSONField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)

class Order(models.Model):
    contact_name = models.CharField()
    contact_email = models.CharField(null=True)
    contact_phone = models.CharField(null=True)
    message = models.TextField(null=True)
    company = models.CharField(null=True)
    inn = models.CharField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_type = models.CharField(choices=ORDER_TYPE)
    order_status = models.CharField(choices=ORDER_STATUS)
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)