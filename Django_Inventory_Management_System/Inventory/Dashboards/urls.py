from django.urls import path
from .views import index, staff


urlpatterns = [
    path('',index, name= 'index' ),
    path('staff/', staff, name= 'staff')
]