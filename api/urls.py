from django.urls import path
from .views import GeminiChatAPIView , register



urlpatterns = [
     path("gemini/chat/", GeminiChatAPIView.as_view(), name="gemini_chat"),
     path("register/",register,name="register"),
     path("register/<int:id>/",register,name="register"),
]