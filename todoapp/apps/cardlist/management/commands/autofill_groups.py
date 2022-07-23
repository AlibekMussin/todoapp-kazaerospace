from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'just execute this command and check groups at admin'

    def handle(self, *args, **options):
        # Создание дефолтных групп приложения
        Group.objects.get_or_create(name='cardlist_admin')
        Group.objects.get_or_create(name='cardlist_user')