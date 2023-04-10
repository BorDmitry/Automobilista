from django.urls import path
from . import views


# страница полезных советов
urlpatterns = [
    path('car_tips/', views.tips, name='tips'),
]
