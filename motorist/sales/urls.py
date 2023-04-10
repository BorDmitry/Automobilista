from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                          #  Главная/ реклама внедорожников
    path('cars/', views.cars, name='cars'),                       #  Автосалон
    path('car/<str:pk>/', views.car, name='car'),                 #  подробный просмотр  авто
    path('news/', views.news, name='news'),                 #  подробный просмотр  авто

    # path('create/', views.create_order, name='create_order'),   #  создание заказа клиентом автосалона
    path('private_car/', views.private_car, name='private_car'),  #  объявления продаж авто частников
]
