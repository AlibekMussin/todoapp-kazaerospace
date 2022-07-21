# Vendor
from datetime import datetime

# Local
from todoapp.apps.cardlist.models import CardNotification


def check_notifications(request, card):
    """ Проверка непрочитанных отправленных уведомлений по карточке и их прочитывание """
    user = request.user
    CardNotification.objects.filter(
        card_executor=user,
        is_read=False,
        is_sent=True
    ).update(
        is_read=True,
        read_at=datetime.now()
    )