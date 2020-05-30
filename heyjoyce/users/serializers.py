from django.utils.translation import gettext as _
from django.conf import settings
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    extra_kwargs = {
        'email': {'allow_null': False, 'required': True}
    }

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'about')
