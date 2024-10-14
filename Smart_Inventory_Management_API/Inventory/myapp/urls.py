from django.urls import path
from .views import home, ProductsView, ProductViewItem


urlpatterns = [
    path('', home, name='home'),
    path('menu/', ProductsView.as_view(), name= 'ProductsView'),
    path('menu/<int:pk>', ProductViewItem.as_view(), name= 'ProductViewItem'),
]