"""AC_ERP_PH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Usuario/', include('Usuario.urls')),
    url(r'^Modulo/', include('Modulo.urls')),
    url(r'^Cobro/', include('Cobro.urls')),
    url(r'^Comprobante/', include('Comprobante.urls')),
    url(r'^CuentaCobro/', include('CuentaCobro.urls')),
    url(r'^Parametro/', include('Parametro.urls')),
    url(r'^HistoricoParametro/', include('HistoricoParametro.urls')),
    url(r'^UnidadPrivada/', include('UnidadPrivada.urls')),
    url(r'^Noticia/', include('Noticia.urls')),
]
