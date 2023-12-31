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
from .views import load_login, load_forgot_password, load_new_password

urlpatterns = [
    path('', load_login, name='loadlogin'),
    path('esqueceu-a-senha/', load_forgot_password, name='forgotpassword'),
    path('esqueceu-a-senha/nova-senha/', load_new_password, name='newpassword'),
]