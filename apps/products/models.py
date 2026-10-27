from django.contrib.auth import get_user_model
from django.db import models




class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.RESTRICT,
        related_name="orders",
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Quantity {self.quantity} order {self.order.name} product {self.product.name}"



class Article(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.RESTRICT,
        related_name="articles",
    )
    description = models.TextField()
    photo = models.ImageField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
