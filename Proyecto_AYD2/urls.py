# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from Sysforum.views import list_temas, add_tema, ver_tema


urlpatterns = [
    # Examples:
    # url(r'^$', 'Proyecto_AYD2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include(('dashboard.urls', 'dashboard'), namespace='dash')),
    url(r'^tema/list/', list_temas, name='list_temas'), #listado
    url(r'^tema/add/', add_tema, name='add_tema'), #formulario para añadir
    url(r'^ver/(?P<pk>\d+)$', ver_tema, name='ver'), 

]
