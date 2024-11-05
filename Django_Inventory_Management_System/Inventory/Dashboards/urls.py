from django.urls import path
from .views import index, staff, orders, products, product_delete, product_update


urlpatterns = [
    path('',index, name= 'dashboards-index' ),
    path('staff/', staff, name= 'dashboards-staff'),
    path('orders/', orders, name= 'dashboards-orders'),
    path('products/', products, name= 'dashboards-products'),
    path('products/Delete/<int:pk>/', product_delete, name= 'dashboards-product-delete'),
    path('products/Edit/<int:pk>/', product_update, name= 'dashboards-product-update'),
]