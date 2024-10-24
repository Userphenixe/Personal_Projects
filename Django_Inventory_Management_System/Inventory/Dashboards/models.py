from django.db import models
from django.contrib.auth.models import User


CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food',  'Food'),
)

class Product(models.Model):
    name  = models.CharField(max_length=200, null= True)
    category = models.CharField(max_length=200,  choices=CATEGORY, null= True)
    quantity = models.PositiveIntegerField(null= True)

    class  Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Staff Products'


    def  __str__(self):
        return f"{self.name}-{self.quantity}"
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null= True)
    order_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Staff Orders'

    def __str__(self):
        return f"{self.product} order by {self.staff.username} on  {self.order_date}"
