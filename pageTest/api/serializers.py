from rest_framework import serializers
from pageTest.models import Inventory
from django.contrib.auth.models import User

class InventorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventory
        fields = "__all__"
    
    def create(self, validated_data):
        return Inventory.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"