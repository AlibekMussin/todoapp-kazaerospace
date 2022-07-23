# Vendor
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from datetime import datetime, timezone
import jwt
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Local
from todoapp.apps.user.serializers import LoginSerializer
from .utils import generate_token


class LoginView(GenericViewSet):
    serializer_class = LoginSerializer
    permission_classes = ()
    http_method_names = ('post',)

    def create(self, request, *args, **kwargs):
        """Логиним пользователя в систему"""
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response({'error_code': 'VALIDATION_ERROR',
                             'detail': serializer.errors},
                            status=400)

        username = serializer.data.get('username')
        password = serializer.data.get('password')

        user = authenticate(request=request,
                            username=username,
                            password=password)

        if user:
            access = generate_token(
                user,
                settings.JWT_ACCESS_TOKEN_LIFETIME,
            )
            refresh = generate_token(
                user,
                settings.JWT_REFRESH_TOKEN_LIFETIME,
                'refresh'
            )

            return Response({'access': access,
                             'refresh': refresh})
        else:
            return Response(data={'error_code': 'AUTHENTICATION_FAILED',
                                  "detail": "Неверный логин или пароль"},
                            status=403)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer