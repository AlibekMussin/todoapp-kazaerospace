# Generated by Django 4.0.6 on 2022-07-20 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardlist', '0003_card_deleted_by_user_cardexecutor_deleted_by_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardexecutor',
            options={'ordering': ['-id'], 'verbose_name': 'Исполнитель задачи', 'verbose_name_plural': 'Исполнители задач'},
        ),
    ]
