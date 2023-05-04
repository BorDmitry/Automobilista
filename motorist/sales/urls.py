from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),                             #  Главная/ реклама внедорожников

    path('cars/', views.cars, name='cars'),                          #  Автосалон
    path('single_car/<str:pk>/', views.car, name='car'),             #  подробный просмотр  авто

    path('newss/', views.newss, name='newss'),                       #  подробный просмотр  авто
    path('news/<str:pk>/', views.news, name='news'),                 #  подробный просмотр  авто

    path('test_drive/', views.test_drive, name='test_drive'),        #  подробный просмотр  авто

    path('create-client/', views.create_client, name='create-client'),      #  создание заказа клиентом автосалона
]
