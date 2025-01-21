from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Menu, Booking
from rest_framework.authtoken.models import Token
import json

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(Name="Hamza", No_of_guests= 8)
        self.assertEqual(str(item), "Hamza")
class MenuViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        Menu.objects.create(Title="Pizza", Price=10.99, Inventory=50)
        Menu.objects.create(Title="Burger", Price=8.99, Inventory=30)
        Menu.objects.create(Title="Pasta", Price=12.50, Inventory=20)

    def test_getall(self):
        response = self.client.get(reverse('MenuItemsView'))
        expected_data = [
            {'id': Menu.objects.get(Title="Pizza").id, 'Title': 'Pizza', 'Price': '10.99', 'Inventory': 50},
            {'id': Menu.objects.get(Title="Burger").id, 'Title': 'Burger', 'Price': '8.99', 'Inventory': 30},
            {'id': Menu.objects.get(Title="Pasta").id, 'Title': 'Pasta', 'Price': '12.50', 'Inventory': 20},
        ]
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, expected_data)

class SingleMenuItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.menu_item = Menu.objects.create(Title="Pizza", Price=10.99, Inventory=50)

    def test_get_single_menu_item(self):
        response = self.client.get(reverse('SingleMenuItemView', args=[self.menu_item.id]))
        self.assertEqual(response.status_code, 200)

    def test_update_menu_item(self):
        updated_data = {'Title': 'Pizza Updated', 'Price': 12.99, 'Inventory': 40}
        response = self.client.put(reverse('SingleMenuItemView', args=[self.menu_item.id]), data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item.refresh_from_db()
        self.assertEqual(self.menu_item.Title, 'Pizza Updated')

    def test_delete_menu_item(self):
        response = self.client.delete(reverse('SingleMenuItemView', args=[self.menu_item.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 0)