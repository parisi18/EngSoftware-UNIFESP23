from django.urls import path
from .views import register_request

urlpatterns = [
    path('user/', register_request, name='register')
]