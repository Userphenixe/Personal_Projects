from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group

admin.site.site_header = 'KeyInventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'category', 'Quantity', )
    list_filter = ['category']
    search_fields = ['Name', 'category']

admin.site.unregister(Group)
admin.site.register(Product)
