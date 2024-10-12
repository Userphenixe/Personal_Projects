from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer, Supplier, Category, Product, Order

class SerializerCustomer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SerializerSupplier(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SerializerProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SerializerOrder(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']