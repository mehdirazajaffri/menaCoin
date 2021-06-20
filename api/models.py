from django.db import models

# Create your models here.
from solo.models import SingletonModel


class ExchangeRate(SingletonModel):
    btc_rate = models.DecimalField(max_digits=20, decimal_places=10, blank=False, null=False)

    def __str__(self):
        return f"BTC/USD Rate Is {self.btc_rate}"

    class Meta:
        verbose_name = "BTC Exchange Rate"
