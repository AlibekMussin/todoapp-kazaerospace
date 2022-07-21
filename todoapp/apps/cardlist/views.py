# Vendor
from datetime import datetime
from django.db.transaction import atomic
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

# Local
from todoapp.apps.utils import permissions
from todoapp.apps.cardlist.models import Card, CardExecutor, CardNotification
from todoapp.apps.cardlist.serializers import CardGetSerializer, CardListSerializer, CardCreateSerializer
from todoapp.apps.utils import utils as app_utils
from rest_framework import filters
from django.contrib.auth.models import User


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
        with atomic():

            request.data['created_by_user'] = request.user.id   # Автоматически указываем создавшего юзера
            executors = request.data.pop('executors')
            serializer = CardCreateSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            new_card = serializer.save()
            for executor in executors:
                executor_obj = User.objects.filter(id=executor.get('executor')).last()
                if executor_obj:
                    new_card_executor = CardExecutor.objects.create(
                        card=new_card,
                        executor=executor_obj,
                        created_by_user=request.user
                    )
                    notifications = executor.get('notifications')
                    for notification in notifications:
                        CardNotification.objects.create(
                            card_executor=new_card_executor,
                            notif_datetime=notification.get('notif_datetime', None),
                            created_by_user=request.user
                        )

            headers = self.get_success_headers(new_card)
            return Response(CardGetSerializer(new_card).data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        """ Получить список только моих карточек"""
        user = request.user
        cards = self.queryset.filter(executors__executor=user)
        data = self.get_serializer(cards, many=True).data
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        """ При гете надо проверять, является ли пользователь создателем карточки, её исполнителем либо админом """
        user = request.user
        card = self.get_object()
        if not card.executors.filter(executor=user).exists() and card.created_by_user != user:
            if not app_utils.is_cardlist_admin(request):
                raise APIException(
                    detail='У вас нет разрешения на просмотр данной карточки',
                    code='403;NOT_YOUR_CARD')

        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """ При гете надо проверять, является ли пользователь создателем карточки, её исполнителем либо админом """
        user = request.user
        card = self.get_object()
        if not card.executors.filter(executor=user).exists() and not card.created_by_user == user:
            if not app_utils.is_cardlist_admin(request):
                raise APIException(
                    detail='У вас нет разрешения на редактирование данной карточки',
                    code='403;NOT_YOUR_CARD')

        request.data['updated_by_user'] = request.user.id
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        with atomic():
            pk = kwargs.get('pk')
            card = self.get_object()
            card.deleted_by_user = request.user
            card.deleted_at = datetime.now()
            card.is_deleted = True
            executors = card.executors.all()

            for executor in executors:
                notifications = executor.notifications.all()
                for notification in notifications:
                    notification.is_deleted = True
                    notification.deleted_at = datetime.now()
                    notification.deleted_by_user = self.request.user
                    notification.save()
                executor.is_deleted = True
                executor.deleted_at = datetime.now()
                executor.deleted_by_user = self.request.user
                executor.save()

            card.save()
            return Response(status=204)


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

