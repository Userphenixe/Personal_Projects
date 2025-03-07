from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, Menu

class SerializerMenu(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'Title', 'Price', 'Inventory']
        extra_kwargs = {'Price': {'min_value': 2.00},
                        'Inventory': {'min_value': 0.00}}
        
class SerializerBooking(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields =  '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']