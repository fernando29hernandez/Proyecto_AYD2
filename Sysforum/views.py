# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from Sysforum.models import Tema
from Sysforum.forms import *

from django.contrib import messages
from django.http import HttpResponse

def list_temas(request):
    return render(request,"listar_temas.html", {"temas": Tema.objects.all(), "messages": messages.get_messages(request)})


def add_tema(request):
    form = TemaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The post has been saved!")
            return HttpResponseRedirect("/tema/list/")
    return render(request, 'crear_tema.html', {'form': form})
