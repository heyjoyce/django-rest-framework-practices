import pytest
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_get_user(api_client, create_user):
   user = create_user(username='someone', email='someone@gmail.com')
   assert user.password

   response = api_client.get('/api/v1/users/')
   assert response.status_code == 200
   assert len(response.data['results']) == 1
