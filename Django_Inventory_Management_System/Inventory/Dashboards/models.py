from django.db import models

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food',  'Food'),
)

class Product(models.Model):
    Name  = models.CharField(max_length=200, null= True)
    category = models.CharField(max_length=200,  choices=CATEGORY, null= True)
    Quantity = models.PositiveIntegerField(null= True)

    def  __str__(self):
        return f"{self.Name}-{self.Quantity}"