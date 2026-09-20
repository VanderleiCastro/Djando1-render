from django import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import context
from django.http import HttpResponse
from django.template import loader

from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso' : 'Programação Web com Django Framework',
        'outro' : 'Django é massa!',
        'produtos':produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request,pk):
#    prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto':prod
    }
    return render(request,'produto.html',context)

def pagina_nao_encontrada(request,exception):
    """trata o erro 404"""
    return render(request,'404.html',status=404)

def erro_interno_servidor(request):
    """trata o erro 500"""
    return render(request,'500.html',status=500)

'''def error404(request,exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),content_type='text/html; charset=utf8', status=500)'''