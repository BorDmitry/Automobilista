from django.urls import path
from . import views

urlpatterns = [
    path('inbox_chat/', views.inbox_chat, name='inbox_chat'),
]
