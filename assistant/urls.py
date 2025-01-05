from django.urls import path
from .views import assistant, chat_send_message, create_thread

urlpatterns = [
    path("", assistant, name="assistant"),
    path("messages/send", chat_send_message, name="chat_send_message"),
    path("messages/thread", create_thread, name="create_thread"),
]
