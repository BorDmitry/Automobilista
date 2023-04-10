from django.urls import path
from . import views

urlpatterns = [
    path('service_top/', views.service_top, name='service_top'),   #  обслуживание
]
