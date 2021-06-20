from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r"quotes", views.GetExchangeRates, basename="GetExchangeRate")

urlpatterns = [
    path("v1/", include(router.urls)),
]
