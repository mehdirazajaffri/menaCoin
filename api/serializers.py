from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import ExchangeRate


class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = get_user_model()(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        exclude = ("id",)
