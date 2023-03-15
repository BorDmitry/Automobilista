from django.urls import path, include
from registr import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', views.signupuser, name="signupuser"),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
