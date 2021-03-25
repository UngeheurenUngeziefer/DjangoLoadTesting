from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message
from .serializers import MessageSerializer


class MessageView(APIView):

    def get(self, request):
        messages = Message.objects.all()
        '''the many param informs the serializer that it will be serializing
		more than a single item'''
        serializer = MessageSerializer(messages, many=True)
        return Response({"messages": serializer.data})


    def post(self, request):
        message = request.data


        # Create an mesage from the above data
        serializer = MessageSerializer(data=message)
        if serializer.is_valid(raise_exception=True):
            message_saved = serializer.save()
            succsess_str = f"Message {message_saved.title} created successfully"
        return Response({"success": succsess_str})