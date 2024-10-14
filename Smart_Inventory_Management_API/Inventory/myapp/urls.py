from django.urls import path
from .views import home, ProductsView, ProductViewItem, SuppliersView, SupplierViewItem, CategoriesView, CategoryViewItem, CustomerListView, OrderListView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', home, name='home'),
    path('menu/', ProductsView.as_view(), name= 'ProductsView'),
    path('menu/<int:pk>', ProductViewItem.as_view(), name= 'ProductViewItem'),
    path('suppliers/', SuppliersView.as_view(), name='SuppliersView'),
    path('suppliers/<int:pk>', SupplierViewItem.as_view(), name='SupplierViewItem'),
    path('categories/', CategoriesView.as_view(), name='CategoriesView'),
    path('categories/<int:pk>', CategoryViewItem.as_view(), name='CategoryViewItem'),
    path('customers/', CustomerListView.as_view(), name= 'CustomerListView'),
    path('orders/', OrderListView.as_view(), name='OrderListView'),
    path('api-token-auth/', obtain_auth_token),
]