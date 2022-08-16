from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .views import UserLogin, UserSignUp

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('signup/', UserSignUp.as_view(), name='signup'),
]