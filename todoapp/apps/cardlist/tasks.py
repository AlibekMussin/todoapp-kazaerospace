from django.utils import timezone
from datetime import timedelta, datetime

from celery import task
from celery import shared_task
from todoapp.apps.cardlist.models import CardNotification
from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(run_every=crontab(hour=0, minute=1))
def send_notifications():

    notifs = CardNotification.objects.filter(
        is_sent=False,
        notif_datetime__lte=datetime.now()
    )
    for notif in notifs:
        notif.is_sent = True
        notif.updated_at = datetime.now()
        notif.save()

    return True
