from django.db import models
from django.core.exceptions import ValidationError

class Supplier(models.Model):
    name = models.CharField(max_length= 255)
    email = models.EmailField(unique = True, max_length=255)
    phone_number = models.CharField(unique = True, max_length= 10)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    unit_stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete= models.PROTECT, related_name='products')
    supplier = models.ForeignKey(Supplier, on_delete= models.PROTECT, related_name='products')

    def __str__(self):
        return self.name
    
    def decrement_stock(self, quantity):
        if self.unit_stock >= quantity:
            self.unit_stock -= quantity
            self.save()
            if self.unit_stock == 0:
                print(f"Warning: The stock of {self.name} is now empty!")
        else:
            raise ValidationError(f"Not enough stock for {self.name}. Available: {self.unit_stock}")
        
    def is_available(self):
        return self.unit_stock > 0

class Customer(models.Model):
    name = models.CharField(max_length= 255)
    email = models.EmailField(unique = True, max_length=255)
    phone_number = models.CharField(unique = True, max_length= 10)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
       STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
        ]
       customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')
       products = models.ManyToManyField(Product, related_name='products')
       order_date = models.DateField()
       status = models.CharField(max_length=255, choices= STATUS_CHOICES, default= 'Pending')
       order_price = models.DecimalField(max_digits=10, decimal_places= 2)
       created_at = models.DateField(auto_now_add=True)

       def __str__(self):
        return f"Order {self.id} - {self.customer.name}"
       
       def calculate_order_price(self):
        total_price = sum([product.price for product in self.products.all()])
        return total_price
       
       def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        for product in self.products.all():
            if product.is_available():
                product.decrement_stock(1)
            else:
                raise ValidationError(f"The product {product.name} is out of stock and cannot be ordered.")
