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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from httperrors import views

# rotas de status http 200
urlpatterns = [
    path("admin/", admin.site.urls),
    path('animais/', include('imageupload.urls'), name='animals'),
    path('', include('home.urls'), name='home'),
    path('sobre-nos/', include('aboutus.urls'), name='aboutus'),
    path('api/', include('newsletter.urls')),
    path('entrar/', include('login.urls'), name='login'),
    path('fale-conosco/', include('contactus.urls'), name='contactus'),
    path('prediction/', include('prediction.urls')),
    path('register/', include('userRegister.urls')),
    path('perfil/', include('perfilscreen.urls')),
    path('accounts/', include('allauth.urls')),
]

# rotas de status de erro http
handler401 = views.error_401_page
handler400 = views.error_400_page
handler403 = views.error_403_page
handler404 = views.error_404_page
handler500 = views.error_500_page

# essa configuracao permite o django servir imagens de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)