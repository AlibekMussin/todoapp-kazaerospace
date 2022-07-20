# Vendor
from rest_framework.serializers import ModelSerializer

# Local
from todoapp.apps.cardlist.models import Card, CardExecutor


# seralizers for card executors
class CardExecutorCreateSerializer(ModelSerializer):
    class Meta:
        model = CardExecutor
        fields = [
            'subject',
            'description',
            'status'
        ]


class CardExecutorListSerializer(ModelSerializer):
    class Meta:
        model = CardExecutor
        fields = [
            'id',
            'subject',
            'description',
            'status'
        ]


class CardExecutorGetSerializer(ModelSerializer):
    class Meta:
        model = CardExecutor
        fields = [
            'id',
            'subject',
            'description',
            'status'
        ]


class CardExecutorUpdateSerializer(ModelSerializer):
    class Meta:
        model = CardExecutor
        fields = [
            'id',
            'subject',
            'description',
            'status'
        ]


# seralizers for cards
class CardCreateSerializer(ModelSerializer):
    executors = CardExecutorCreateSerializer()

    class Meta:
        model = Card
        fields = [
            'subject',
            'description',
            'status'
        ]


class CardListSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'subject',
            'description',
            'status',
            'created_by_user'
        ]


class CardGetSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'subject',
            'description',
            'status',
            'created_by_user'
        ]


class CardUpdateSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'subject',
            'description',
            'status',
            'updated_by_user'
        ]