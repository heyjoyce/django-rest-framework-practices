import uuid
import pytest
from django.contrib.auth.models import User

@pytest.fixture
def test_password():
   return 'strong-test-pass'
  
@pytest.fixture
def create_user(db, django_user_model, test_password):
   def make_user(**kwargs):
       kwargs['password'] = test_password
       if 'username' not in kwargs:
           kwargs['username'] = str(uuid.uuid4())
       return django_user_model.objects.create_user(**kwargs)
   return make_user

@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()