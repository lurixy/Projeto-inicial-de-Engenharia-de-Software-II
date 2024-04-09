from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('index/', IndexView.as_view(), name="index"),
]
