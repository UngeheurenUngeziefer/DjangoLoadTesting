from django.urls import path
from .views import MessageView

app_name = 'messages'

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('messages/', MessageView.as_view()),
]