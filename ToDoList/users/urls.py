from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login.as_view(), name='login'),
    path('register', views.register.as_view(), name='register')
]