from rest_framework.test import APITestCase
from rest_framework import status


class UserTests(APITestCase):
    def test_create_user(self):
        body = {'username': 'guest', 'email': 'guest@host.com'}
        response = self.client.post('/api/v1/users', body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
