from rest_framework import serializers
from .models import Points


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ['id', 'lat', 'lng', 'DeBe']
