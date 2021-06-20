from django.contrib.auth.models import User
from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import ExchangeRate
from .serializers import ExchangeRateSerializer, UserSerializer
from .services import get_current_btc_exchange_rate, get_exchange_rate


class GetExchangeRates(viewsets.ModelViewSet):
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            get_current_btc_exchange_rate()
            print("Data updated",get_exchange_rate())
            return Response(ExchangeRateSerializer(get_exchange_rate()).data, status=status.HTTP_201_CREATED)
        except:
            return Response("ERROR", status=status.HTTP_503_SERVICE_UNAVAILABLE)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
