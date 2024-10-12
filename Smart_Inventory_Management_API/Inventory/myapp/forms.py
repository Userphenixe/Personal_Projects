from django.forms import ModelForm
from .models import Customer, Order

class FormCustomer(ModelForm):
    class Meta:
        name = Customer
        fields = '__all__'

class FormOrder(ModelForm):
    class Meta:
        name = Order
        fields = '__all__'

