from datetime import datetime
from django.db import models, transaction
from django.contrib.auth.models import User


class DeleteManager(models.Manager):
    """
    Объекты не удаляются из БД,
    а помечаются как удаленные и фильтруются только неудаленные
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class CommonFields(models.Model):
    """
    Содержит мета-информацию о наследующих моделях -
    кто создал, когда создал и пометка на удаление
    """

    class Meta:
        abstract = True

    created_by_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Создатель',
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True,
        editable=False,
        db_index=True
    )
    updated_by_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Кто обновил запись',
        null=True, blank=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True,
        editable=False,
        db_index=True
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        editable=False,
        db_index=True
    )
    deleted_at = models.DateTimeField(
        verbose_name='Когда удалена запись',
        editable=False,
        null=True, blank=True
    )

    objects = DeleteManager()

    def delete(self, using=None, keep_parents=False):
        if self.is_deleted:
            return
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()
