from rest_framework import serializers
from .models import *

class laptop_serializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'