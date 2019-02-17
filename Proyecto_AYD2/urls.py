# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from Sysforum import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Proyecto_AYD2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dashboard/', include('dashboard.urls', namespace = 'dash')),
    url(r'^tema/list/', 'Sysforum.views.list_temas', name='list_temas'), #listado
    url(r'^tema/add/', 'Sysforum.views.add_tema', name='add_tema'), #formulario para añadir
    
]
