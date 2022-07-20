# Vendor
import jwt
from datetime import datetime, timezone
from django.conf import settings
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

# Local
from .serializers import VerifySerializer


def verify_token(token, token_type='access'):
    """Проверка токена"""
    try:
        decoded_jwt = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=(settings.JWT_ALGORITHM,)
        )
    except (jwt.exceptions.ExpiredSignatureError,
            jwt.exceptions.InvalidSignatureError,
            jwt.exceptions.DecodeError):
        return None

    if decoded_jwt['token_type'] != token_type:
        return None

    return decoded_jwt


def generate_token(user, exp_time, token_type='access'):
    """
    генерируем ресет токен для сброса пароля
    :param user: объект класса User (app.models)
    :param exp_time: срок токена в datetime.timedelta
    :param token_type: тип токена
    """
    expire_date = round((datetime.now(tz=timezone.utc) + exp_time).timestamp())

    body = {
        'token_type': token_type,
        'exp': expire_date,
        'user_id': user.id,
        'email': user.email,
        'username': user.username,
        'is_superuser': user.is_superuser,
        'is_staff': user.is_staff
    }
    encoded_body = jwt.encode(
        body,
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return encoded_body.decode('utf-8')


class VerifyView(GenericViewSet):
    permission_classes = ()
    serializer_class = VerifySerializer

    def verify(self, request, *args, **kwargs):
        """Проверяем действительность токена"""
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response({'error_code': 'VALIDATION_ERROR',
                             'detail': serializer.errors},
                            status=400)

        verified_token = verify_token(
            serializer.data.get('token'),
            'access'
        )
        if not verified_token:
            return Response({'error_code': 'INVALID_TOKEN'},
                            status=401)

        return Response(verified_token)