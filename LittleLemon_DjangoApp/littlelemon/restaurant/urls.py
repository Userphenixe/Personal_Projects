from django.urls import path
from .views import home, about, book, BookingListView, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('book/', book, name='book'),
    path('reservations/', BookingListView.as_view(), name='BookingListView'),
    path('menu/', MenuItemsView.as_view(), name='MenuItemsView'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name = 'SingleMenuItemView'),
    path('api-token-auth/', obtain_auth_token),
]