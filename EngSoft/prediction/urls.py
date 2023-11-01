from django.urls import path
from .views import image_view

urlpatterns = [
    path('image/', image_view, name='image'), # change this to your desired URL path
]
