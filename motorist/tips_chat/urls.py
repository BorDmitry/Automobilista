from django.urls import path
from . import views

urlpatterns = [
    path('tips_chat/', views.tips_chat, name='tips_chat'),
]
