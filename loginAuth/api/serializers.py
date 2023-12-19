from rest_framework import serializers
from django.contrib.auth.models import User

class userSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        return User.objects.create(**validated_data)