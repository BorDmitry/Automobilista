from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sales'),                         #  реклама внедорожников
    path('cars/', views.cars, name='cars'),                    #  автосалон
    path('currentcar/', views.currentcar, name='currentcar'),  # подробный просмотр определлённого авто
    path('create/', views.create_order, name='create_order'),  # создание заказа клиентом автосалона
    path('private_car/', views.private_car_sales, name='private_car_sales'),  # объявления продаж авто частников
]
