from rest_framework import serializers
from pageTest.models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventory
        fields = "__all__"
    
    def create(self, validated_data):
        return Inventory.objects.create(**validated_data)
