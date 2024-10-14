from django.forms import ModelForm
from .models import Customer, Order

class FormCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class FormOrder(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
