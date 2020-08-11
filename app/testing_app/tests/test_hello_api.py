from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


TAGS_URL = reverse('testing_app:hello-viewset-list')


class HelloApiTests(TestCase):
    """Test the Hello API"""

    def setUp(self):
        self.client = APIClient()

    def test_hello_api(self):
        """Test that API return OK and desired response"""
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['message'], 'Hello!')
