from django.shortcuts import render
from django.http import HttpResponse
from .serializers import SerializerProduct, SerializerSupplier, SerializerCategory, SerializerCustomer, SerializerOrder
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .forms import FormCustomer, FormOrder
from .models import Product, Supplier, Category, Customer, Order
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime

def home(request):
    return HttpResponse('Welcome!')

class CustomerListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        date = request.GET.get('date', datetime.today().date())
        customers = Customer.objects.all()
        serializer = SerializerCustomer(customers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SerializerCustomer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        date = request.GET.get('date', datetime.today().date())
        orders = Order.objects.all()
        serializer = SerializerOrder(orders, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer =SerializerOrder(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = SerializerProduct

class ProductViewItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = SerializerProduct

class SuppliersView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SerializerSupplier

class SupplierViewItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SerializerSupplier

class CategoriesView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = SerializerCategory

class CategoryViewItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = SerializerCategory
