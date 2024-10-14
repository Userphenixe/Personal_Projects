from django.urls import path
from .views import home, ProductsView, ProductViewItem, SuppliersView, SupplierViewItem


urlpatterns = [
    path('', home, name='home'),
    path('menu/', ProductsView.as_view(), name= 'ProductsView'),
    path('menu/<int:pk>', ProductViewItem.as_view(), name= 'ProductViewItem'),
    path('suppliers/', SuppliersView.as_view(), name='SuppliersView'),
    path('suppliers/<int:pk>', SupplierViewItem.as_view(), name='SupplierViewItem'),
]