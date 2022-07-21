# Generated by Django 4.0.6 on 2022-07-21 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cardlist', '0005_alter_card_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Обновлено')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False, verbose_name='Удалено')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Когда удалена запись')),
                ('notif_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время уведомления')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано ли исполнителем')),
                ('read_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Когда прочитано уведомление')),
                ('card_executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifications', to='cardlist.cardexecutor', verbose_name='Связь с исполнителем')),
                ('created_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('deleted_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Кто удалил запись')),
                ('updated_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Кто обновил запись')),
            ],
            options={
                'verbose_name': 'Время уведомления по задаче',
                'verbose_name_plural': 'Время уведомления по задаче',
            },
        ),
    ]