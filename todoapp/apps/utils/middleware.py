import requests
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import (
    SuspiciousOperation,
    ObjectDoesNotExist,
    ValidationError
)
from rest_framework.exceptions import APIException
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

# Local
from todoapp.apps.user import utils as user_utils

class DisableCSRF(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

class AuthenticationMiddleware(MiddlewareMixin):
    def get_auth_header(self, request):
        """Получить токен из хидера"""
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            request.employee = None
            request.organization = None
            return
        token = auth_header.split()
        if len(token) != 2:
            raise SuspiciousOperation("Invalid auth header")

        return token[1]

    def process_request(self, request):
        """Отправка токена для верификации на авторизационный сервис"""
        token = self.get_auth_header(request)
        if not token:
            return

        body = user_utils.verify_token(token)

        if body is None:
            raise APIException(
                detail='Токен не верифицирован',
                code='403;TOKEN_NOT_VERIFIED'
            )
        try:
            try:
                user = User.objects.get(id=body['user_id'])
            except ObjectDoesNotExist:
                user = User.objects.create(
                    id=body['user_id'],
                    is_superuser=body['is_superuser'],
                    is_staff=body['is_staff'],
                    email=body['email'],
                    username=body['email']
                )
            request.user = user

        except ObjectDoesNotExist:
            raise APIException(
                detail='Ошибка авторизации',
                code='403;AUTHORIZATION_ERROR'
            )