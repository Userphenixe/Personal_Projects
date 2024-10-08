from django.db import models

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
