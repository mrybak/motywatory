from motywatory.models import Motivator
from rest_framework import serializers


class MotivatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Motivator
        fields = ('url', 'text')

