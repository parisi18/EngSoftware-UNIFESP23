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
# sao caminhos completos para views que lidam com esses status http por padrao no Django
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path("admin/", admin.site.urls),
    path('animais/', include('imageupload.urls'), name='animals'),
    path('', include('home.urls'), name='home'),
    path('sobre-nos/', include('aboutus.urls'), name='aboutus'),
    path('api/', include('newsletter.urls')),
    path('entrar/', include('login.urls'), name='login'),
    path('fale-conosco/', include('contactus.urls'), name='contactus')
]

# essa configuracao permite o django servir imagens de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# configuracao das views que vao processar essa requisicao
handler401 = 'httperrors.views.error_401_page'
handler400 = 'httperrors.views.error_400_page'
handler403 = 'httperrors.views.error_403_page'
handler404 = 'httperrors.views.error_404_page'
handler500 = 'httperrors.views.error_500_page'