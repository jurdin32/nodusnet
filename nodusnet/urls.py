"""nodusnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from Abonados.views import reporte_venta
from Inicio.views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('',index, name='index'),
    path('nosotros/',nosotros, name='nosotros'),
    path('planes/',planes, name='planes'),
    path('contacto/',contacto, name='contacto'),
    path('works/',eventos, name='eventos'),
    path('policies/',politicas, name='politicas'),
    path('velocidad/',velocidad,name='velocidad'),
    path('cash/',prueba_pagos, name='cash'),
    path('ok',pago_ok, name='ok'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('report',reporte_venta,name='reporte')
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
