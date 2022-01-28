"""Tests file."""

# Django
from django.utils.http import urlencode

# 3rd-party
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse_lazy
from rest_framework import status

# Project
from pixelshop.models import User, PixelArt


class UserTests(APITestCase):
    """UserTests class."""

    def create_user(self, username, first_name, last_name, email, password, client):
        """User creation function."""
        url = reverse_lazy('api:user-list')
        data = {'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password,
                }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_user(self):
        """Test post and get client function."""
        User.objects.create_superuser(username='admin123', email='admin123@gmail.com', password='admin123')
        client = APIClient()
        client.login(username='admin123', password='admin123')
        new_username = 'gdziekucharek6'
        new_password = 'TamNieMoCoJesc1!'
        new_first_name = 'Robert'
        new_last_name = 'Makłowicz'
        new_email = 'rmaklowicz@gmail.com'
        response = self.create_user(new_username, new_first_name, new_last_name, new_email, new_password, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == 2
        assert User.objects.get(is_superuser=False).first_name == new_first_name
        assert User.objects.get(is_superuser=False).last_name == new_last_name


class PixelArtTests(APITestCase):
    """UserTests class."""

    def create_pixelart(self, title, desc, file, price, client):
        """PixelArt creation function."""
        url = reverse_lazy('api:pixelart-list')
        data = {'title': title,
                'desc': desc,
                'file': file,
                'price': price,
                }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_pixelart(self):
        """Test post and get client function."""
        User.objects.create_superuser(username='admin123', email='admin@admin.com', password='admin123')
        client = APIClient()
        client.login(username='admin123', password='admin123')
        new_title = 'Obrazek testowy'
        new_file = 'static\\images\\fire_in_forest.jpg'
        new_price = 2137.69
        new_desc = 'Opis obrazka testowego.'
        response = self.create_pixelart(new_title, new_desc, new_file, new_price, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert PixelArt.objects.count() == 1
        assert PixelArt.objects.get().title == new_title