from django.urls import path
from .views import index, staff, orders, products


urlpatterns = [
    path('',index, name= 'dashboards-index' ),
    path('staff/', staff, name= 'dashboards-staff'),
    path('orders/', orders, name= 'dashboards-orders'),
    path('products/', products, name= 'dashboards-products')
]