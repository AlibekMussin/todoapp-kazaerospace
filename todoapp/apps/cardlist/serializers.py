# Vendor
from rest_framework.serializers import ModelSerializer

# Local
from todoapp.apps.cardlist.models import Card, CardExecutor
from todoapp.apps.user.serializers import UserGetSerializer

# seralizers for card executors
class CardExecutorCreateSerializer(ModelSerializer):

    class Meta:
        model = CardExecutor
        fields = [
            'card',
            'executor',
        ]


class CardExecutorListSerializer(ModelSerializer):
    executor = UserGetSerializer(read_only=True)

    class Meta:
        model = CardExecutor
        fields = [
            'id',
            'card',
            'executor',
        ]


class CardExecutorGetSerializer(ModelSerializer):
    class Meta:
        model = CardExecutor
        fields = [
            'id',
            'card',
            'executor',
        ]


class CardExecutorUpdateSerializer(ModelSerializer):
    class Meta:
        model = CardExecutor
        fields = [
            'id',
            'card',
            'executor',
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
    executors = CardExecutorListSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = [
            'id',
            'subject',
            'description',
            'status',
            'created_by_user',
            'executors'
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