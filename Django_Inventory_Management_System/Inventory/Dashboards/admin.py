from django.contrib import admin
from .models import Product, Order

admin.site.site_header = 'KeyInventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', )
    list_filter = ['category']
    search_fields = ['name', 'category']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'staff', 'order_quantity', 'order_date', )
    list_filter = ['product', 'order_date']
    search_fields = ['staff', 'order_date']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order,  OrderAdmin)

