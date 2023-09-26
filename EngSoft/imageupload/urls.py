"""
URL configuration for EngSoft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import animal_card, delete_card, edit_card, process_forms, process_search

urlpatterns = [
    path('', animal_card, name='animalcard'),
    path('deletecard/<uuid:animal_id>/', delete_card, name='deletecard'),
    path('editcard/<uuid:animal_id>/', edit_card, name='editcard'),
    path('processforms/', process_forms, name='processforms'),
    path('processearch/', process_search, name='processearch'),
]