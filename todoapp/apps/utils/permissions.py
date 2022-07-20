from rest_framework.permissions import BasePermission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from rest_framework.exceptions import APIException
from . import utils


class ObjectPermission(BasePermission):
    def __init__(self, checker):
        self.checker = checker

    def has_object_permission(self, request, view, object):
        return self.checker(request, view, object)


class IsCardAdmin(BasePermission):
    """Является админом по списку задач"""
    def has_permission(self, request, view):
        if not utils.is_cardlist_admin(request):
            raise APIException('Пользователь не админ', code='401;NO_ADMIN_PERMISSION')
        return True


class IsCardUser(BasePermission):
    """Является обычным пользователем приложения"""
    def has_permission(self, request, view):
        if not utils.is_cardlist_user:
            raise APIException('Пользователь не может совершить данное действие', code='401;NO_PERMISSION')
        return True