from requests import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (
    Currency,
    Unit,
)
from .serializers import (
    CurrencySerializer,
    UnitSerializer,
)


class CurrencyListApi(ListAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    permission_classes = [AllowAny]


class UnitListApi(ListAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
    permission_classes = [AllowAny]
