from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("programs-list")
        self.user = User.objects.create_user("c3po", password="123456")

    def test_authentication_with_right_credentials(self):
        """Test to check user authentication with the right credentials"""
        user = authenticate(username="c3po", password="123456")
        self.assertTrue(user is not None and user.is_authenticated)

    def test_authentication_invalid_username(self):
        """Test to check an invalid username in authentication"""
        user = authenticate(username="c3pp", password="123456")
        self.assertFalse(user is not None and user.is_authenticated)

    def test_authentication_invalid_password(self):
        """Test to check an invalid password in authentication"""
        user = authenticate(username="c3po", password="123455")
        self.assertFalse(user is not None and user.is_authenticated)

    def test_not_allowed_get_request(self):
        """Test to check a not allowed GET request (user not authenticated)"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_allowed_get_request(self):
        """Test to check a allowed GET request (user authenticated)"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
