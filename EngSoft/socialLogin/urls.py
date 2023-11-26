from django.urls import path
from .views import login

urlpatterns = [path("social", login, name="login")]