# Vendor
from django.db import models

# Local
from todoapp.apps.utils.models import CommonFields
from django.contrib.auth.models import User


class CardStatus(models.TextChoices):
    LATER = 'LATER', 'Отложена'
    DOING = 'DOING', 'В работе'
    DONE = 'DONE', 'Исполнена'


class Card(CommonFields):
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Список задач'
        ordering = ['-id']

    subject = models.CharField(
        max_length=255,
        verbose_name='Краткое описание задачи'
    )
    description = models.TextField(
        verbose_name='полное описание задачи',
        null=True, blank=True
    )
    status = models.CharField(
        choices=CardStatus.choices,
        max_length=100,
        verbose_name='Статус задачи',
        default=CardStatus.LATER
    )


# Было принято решение отделить исполнителя от карточки на случай,
# если в будущем понадобится чтобы у карточки было несколько исполнителей
class CardExecutor(CommonFields):
    class Meta:
        verbose_name = 'Исполнитель задачи'
        verbose_name_plural = 'Исполнители задач'
        ordering = ['-id']

    card = models.ForeignKey(
        Card,
        on_delete=models.SET_NULL,
        related_name='executors',
        verbose_name='Связь с карточкой',
        null=True, blank=True
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='cards',
        verbose_name='Исполнитель',
        null=True, blank=True
    )


# Уведомления на таски, может быть много
class CardNotification(CommonFields):
    class Meta:
        verbose_name = 'Время уведомления по задаче'
        verbose_name_plural = 'Время уведомления по задаче'

    card_executor = models.ForeignKey(
        CardExecutor,
        on_delete=models.SET_NULL,
        related_name='notifications',
        verbose_name='Связь с исполнителем',
        null=True, blank=True
    )
    notif_datetime = models.DateTimeField(
        verbose_name='Дата и время уведомления',
        null=True, blank=True
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name='Прочитано ли исполнителем'
    )
    read_at = models.DateTimeField(
        verbose_name='Когда прочитано уведомление',
        editable=False,
        null=True, blank=True
    )