"""Tests file."""

# Django
from django.utils.http import urlencode
from django import urls
from django.test import TestCase

# 3rd-party
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse_lazy
from rest_framework import status

# Project
from pixelshop.models import User, PixelArt
import api.views


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

    def test_post_and_get_client(self):
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
        assert User.objects.count() == 1
        assert User.objects.get().name == new_first_name
        assert User.objects.get().surname == new_last_name


class PixelArtTests(APITestCase):
    """UserTests class."""

    def create_pixelart(self, title, description, price, client):
        """PixelArt creation function."""
        url = reverse_lazy('api:pixelart-list')
        data = {'title': title,
                'desc': description,
                'price': price,
                'certificate_id': None,
                }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_product(self):
        """Test post and get client function."""
        User.objects.create_superuser(username='admin123', email='admin@admin.com', password='admin123')
        client = APIClient()
        client.login(username='admin231', password='admin123')
        new_title = 'Nowy obraz testowy'
        new_price = 2137.0
        new_description = 'Testowy opis nowego obrazu.'
        response = self.create_product(new_title, new_description, new_price, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert PixelArt.objects.count() == 1
        assert PixelArt.objects.get().productname == new_title