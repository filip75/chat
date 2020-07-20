from django.urls import path

from users.views import auth

urls = [
    path('auth/', auth)
]