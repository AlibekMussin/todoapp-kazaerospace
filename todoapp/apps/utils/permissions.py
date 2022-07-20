from rest_framework.permissions import BasePermission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from rest_framework.exceptions import APIException
from . import utils

class IsCardAdmin(BasePermission):
    """Является админом по списку задач"""
    def has_permission(self, request, view):
        if not utils.is_cardlist_admin:
            raise APIException('Пользователь не может совершить данное действие', code='401;NO_PERMISSION')
        return True