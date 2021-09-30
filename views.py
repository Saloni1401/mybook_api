from rest_framework import viewsets

from .serializers import APIAPPSerializer
from .models import APIAPP


class APIAPPViewSet(viewsets.ModelViewSet):
    queryset = APIAPP.objects.all().order_by('name')
    serializer_class = APIAPPSerializer