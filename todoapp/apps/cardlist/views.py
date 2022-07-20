# Vendor
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Local
from todoapp.apps.utils import permissions
from todoapp.apps.cardlist.models import Card, CardExecutor
from todoapp.apps.cardlist.serializers import CardGetSerializer, CardListSerializer


class CardViewSet(viewsets.ModelViewSet):
    """ Вьюшка для карточек с основными операциями """
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
    permissions = {'create': [permissions.IsCardAdmin]}

    def check_permissions(self, request):
        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                self.permission_denied(
                    request,
                    message=getattr(permission, 'message', None),
                    code=getattr(permission, 'code', None)
                )

    def create(self, request, *args, **kwargs):
        request.data['created_by_user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
