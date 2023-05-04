from django.urls import path
from .import views

# Authentific
urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    path('profile/<str:pk>/', views.user_profile, name='user_profile'),
    path('profiles/', views.profiles, name='profiles'),
    path('account/', views.user_account, name='account'),

    path('edit-account/', views.edit_account, name='edit-account'),

]
