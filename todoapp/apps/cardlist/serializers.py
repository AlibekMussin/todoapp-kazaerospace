# Vendor
from django.db.transaction import atomic
from django.contrib.auth.models import User
from rest_framework import serializers

# Local
from todoapp.apps.cardlist.models import Card, CardExecutor
from todoapp.apps.user.serializers import UserGetSerializer


# seralizers for card executors
class CardExecutorCreateSerializer(serializers.ModelSerializer):
    executor = serializers.IntegerField()

    class Meta:
        model = CardExecutor
        fields = [
            'executor',
        ]



class CardExecutorListSerializer(serializers.ModelSerializer):
    executor = UserGetSerializer(read_only=True)

    class Meta:
        model = CardExecutor
        fields = [
            'id',
            'card',
            'executor',
        ]


class CardExecutorGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardExecutor
        fields = [
            'id',
            'card',
            'executor',
        ]


class CardExecutorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardExecutor
        fields = [
            'id',
            'card',
            'executor',
        ]


# seralizers for cards
class CardCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = [
            'subject',
            'description',
            'status'
        ]

    def create(self, validated_data, *args, **kwargs):
        with atomic():
            request = self.context['request']
            validated_data['created_by_user'] = request.user
            card = super().create(validated_data, *args, **kwargs)
            print("card:{}".format(card))
            return card


class CardListSerializer(serializers.ModelSerializer):
    executors = CardExecutorListSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = [
            'id',
            'subject',
            'description',
            'status',
            'created_by_user',
            'updated_by_user',
            'executors'
        ]


class CardGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'subject',
            'description',
            'status',
            'created_by_user'
        ]


class CardUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'subject',
            'description',
            'status',
            'updated_by_user'
        ]