from django.urls import path
from .views import GeminiChatAPIView



urlpatterns = [
     path("gemini/chat/", GeminiChatAPIView.as_view(), name="gemini_chat"),
]