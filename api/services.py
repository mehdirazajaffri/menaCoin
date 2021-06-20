import logging

from django.conf import settings

from api.models import ExchangeRate

logger = logging.getLogger(__name__)

from requests import request

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={}".format(
    settings.ALPHA_KEY)


def get_current_btc_exchange_rate():
    response = request("GET", url)
    sync_exchange_rates(response.json())
    print("Response", response.json())


def sync_exchange_rates(data):
    try:
        if ExchangeRate.objects.count() > 0:
            rate = ExchangeRate.objects.get()
            rate.btc_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
            rate.save()
        else:
            ExchangeRate.objects.create(btc_rate=data.get("5. Exchange Rate"))
    except Exception as e:
        print(e)


def get_exchange_rate():
    try:
        return ExchangeRate.objects.get()
    except:
        return None
