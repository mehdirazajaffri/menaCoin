from rest_framework import serializers

from api.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        exclude = ("id",)
