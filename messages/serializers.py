from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    details = serializers.CharField(max_length=120)
    value = serializers.CharField()
    number = serializers.IntegerField()
    plane_id = serializers.IntegerField()

    def create(self, validated_data):
        return Message.objects.create(**validated_data)