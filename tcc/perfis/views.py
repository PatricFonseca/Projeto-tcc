import datetime
from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')
    #return render(request, "index.html", {'time' : datetime.datetime.now()})

def exibirPerfil(request, perfil_id):
    perfil = Perfil()
    if perfil_id == '1':
        perfil = Perfil('Patric', 'patric.ccomp@gmail.com', '21 9 9341 2341')
    return render(request, "perfil.html", {"perfil": perfil})
