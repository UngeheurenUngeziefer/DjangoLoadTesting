from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Message
from .serializers import MessageSerializer


class MessageView(APIView):

	def get(self, request, pk=None):
		messages = Message.objects.all()
		'''the many param informs the serializer that it will be serializing
		more than a single item'''
		serializer = MessageSerializer(messages, many=True)
		return Response(serializer.data)


	def post(self, request):
		message = request.data


		# Create an mesage from the above data
		serializer = MessageSerializer(data=message)
		if serializer.is_valid(raise_exception=True):
			message_saved = serializer.save()
			success_str = f"Message {message_saved.title} created successfully"
		return Response({"success": success_str})


	def put(self, request, pk):
		saved_message = get_object_or_404(Message.objects.all(), pk=pk)
		data = request.data.get('message')
		serializer = MessageSerializer(instance=saved_message, data=request.data,
																 partial=True)

		if serializer.is_valid(raise_exception=True):
			message_saved = serializer.save()

		success_str = f"Message '{message_saved.title}' updated successfully"
		return Response({"success": success_str})


	def delete(self, request, pk):
	    # Get object with this pk
	    message = get_object_or_404(Message.objects.all(), pk=pk)
	    message.delete()
	    success_str = f"Message with id `{pk}` has been deleted"
	    return Response({"message": success_str}, status=200)



	
