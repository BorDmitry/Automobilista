from django.urls import path
from . import views


urlpatterns = [
    path('', views.commercials, name="commercials"),

    path('salons/', views.salons, name="salons"),
    # path('car/str:pk>/', views.car, name="car"),
    #
    # path('announcement/', views.announcement, name="announcement"),
]
