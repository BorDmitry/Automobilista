from django.urls import path
from . import views

# Authentific
urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    # path('profile/', views.profile, name='profile'),
    path('customer/<str:pk>', views.customer, name='customer'),
]
