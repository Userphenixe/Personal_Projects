from django.shortcuts import render
from django.http import HttpResponse
from .serializers import SerializerProduct, SerializerSupplier
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Product, Supplier

def home(request):
    return HttpResponse('Welcome!')

class ProductsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = SerializerProduct

class ProductViewItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = SerializerProduct

class SuppliersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SerializerSupplier

class SupplierViewItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SerializerSupplier