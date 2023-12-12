from django.db import models

# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]

    product = models.CharField(max_length=100, default="Order")
    customer = models.CharField(max_length=100, default="Customer name")
    quantity_ordered = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id}- {self.product} - {self.customer} - {self.quantity_ordered} units - Status: {self.order_status}"