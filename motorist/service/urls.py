from django.urls import path
from . import views

urlpatterns = [
    path('service_top/', views.service_top, name='service_top'),   #  обслуживание
    path('inbox/', views.inbox, name='inbox'),  # создание заказа клиентом автосалону

    path('review/', views.review, name='review'),  # отзыв клиента автосалона
    path('price_list/', views.price_list, name='price_list'),  # отзыв клиента автосалона
]
