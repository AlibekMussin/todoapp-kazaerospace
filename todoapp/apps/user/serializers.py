# Vendor
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

# Local
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    """Логин в систему"""
    username = serializers.CharField(
        max_length=300,
        required=True
    )
    password = serializers.CharField(
        max_length=128,
        required=True
    )

class VerifySerializer(serializers.Serializer):
    token = serializers.CharField(max_length=4000, required=True)