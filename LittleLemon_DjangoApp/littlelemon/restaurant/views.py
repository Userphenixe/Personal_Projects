from django.shortcuts import render
from .serializers import SerializerMenu, SerializerBooking
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking
from .forms import BookingForm
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

class BookingListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        date = request.GET.get('date', datetime.today().date())
        bookings = Booking.objects.all()
        serializer = SerializerBooking(bookings, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SerializerBooking(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = SerializerMenu

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = SerializerMenu

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = SerializerBooking