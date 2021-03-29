from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from messages.models import Message

def index(request):
	objects = Message.objects.all()

	context = {
		'object_list': objects
	}

	return render(request, 'TestWebSite/index.html', context)