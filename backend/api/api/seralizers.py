from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Events

class ProductSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields= '__all__'