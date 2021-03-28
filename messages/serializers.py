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


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.details = validated_data.get('details', instance.details)
        instance.value = validated_data.get('value', instance.value)
        instance.number = validated_data.get('number', instance.number)
        instance.plane_id = validated_data.get('plane_id', instance.plane_id)

        instance.save()
        return instance