"""
URL configuration for FlashTimes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.pagina_principal, name='pagina_principal'),
    path('Aluguel.html', views.aluguel_page, name='aluguel_page'),
    path('PagarFotoUnica', views.pagar_foto_unica, name='pagar_foto_unica'),
    path('PagarFotoGrupo', views.pagar_foto_grupo, name='pagar_foto_grupo'),
    path('Contato.html', views.contato_page, name='contato_page'),
    path('Email.html', views.email_page, name='email_page'),
    path('politica.html', views.politica_page, name='politica_page'),
]
