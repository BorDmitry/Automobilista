from django.urls import path
from . import views


# Auth
urlpatterns = [
    path('tips/', views.tips, name='tips'),
]
