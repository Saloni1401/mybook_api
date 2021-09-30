from rest_framework import serializers

from .models import APIAPP

class APIAPPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIAPP
        fields = ('name', 'alias')
