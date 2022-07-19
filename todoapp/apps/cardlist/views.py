# Vendor
from rest_framework import viewsets

# Local
from models import Card, CardExecutor

# Create your views here.
class CardViewSet(viewsets.ModelViewSet):
    """Статус формирования акта работодателя"""
    queryset = Card.objects.all()
    serializer_class = FormationActStatusSerializer
