from django.shortcuts import render
from django.http import HttpResponse
from .serializers import SerializerProduct
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Product

def home(request):
    return HttpResponse('Welcome!')

class ProductsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = SerializerProduct

class ProductViewItem(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = SerializerProduct