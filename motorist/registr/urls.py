from django.urls import path, include
from registr import views


urlpatterns = [
    path('signup/', views.signupuser, name="signupuser"),
]
