# Vendor
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Local
from todoapp.apps.utils import permissions
from todoapp.apps.cardlist.models import Card, CardExecutor
from todoapp.apps.cardlist.serializers import CardGetSerializer, CardListSerializer
from todoapp.apps.utils import utils as app_utils
from rest_framework import filters


class CardViewSet(viewsets.ModelViewSet):
    """ Вьюшка для карточек с основными операциями """
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
    permissions = {'create': [permissions.IsCardUser]}

    def check_permissions(self, request):
        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                self.permission_denied(
                    request,
                    message=getattr(permission, 'message', None),
                    code=getattr(permission, 'code', None)
                )

    def create(self, request, *args, **kwargs):
        """ автоматически указываем создавшего юзера"""
        request.data['created_by_user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        """ Получить список только моих карточек"""
        user = request.user
        cards = self.queryset.filter(executors__executor=user)
        data = self.get_serializer(cards, many=True).data
        return Response(data)


class CardAdminViewSet(viewsets.ModelViewSet):
    """ Вьюшка для карточек, с которой работает только админ"""
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
    permission_classes = [permissions.IsCardAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject', 'description', 'status']

    def list(self, request, *args, **kwargs):
        """ Получить список всех карточек"""
        user = request.user
        cards = self.queryset
        qs = self.filter_queryset(cards)
        data = self.get_serializer(qs, many=True).data
        return Response(data)

