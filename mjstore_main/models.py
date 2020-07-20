from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True ,on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=0)
    slug = models.SlugField(max_length=40, unique=True)
    promoted = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to = 'images')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    IN_ORDER = 1
    PENDING = 2
    IN_DELIVERY = 3
    DELIVERED = 4
    CANCELLED = 5
    ORDER_STATUSES = [
        (IN_ORDER, 'In Order'),
        (PENDING, 'Pending'),
        (IN_DELIVERY, 'In delivery'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]
    
    order = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.IntegerField(choices=ORDER_STATUSES, default=IN_ORDER) 
    order_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order)
    