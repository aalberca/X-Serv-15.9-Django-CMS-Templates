from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context, Template, RequestContext

# Create your views here.
login = True
def administrador(request):
    if request.user.is_authenticated():
        login = True
    else:
        login = False;
    return (login)

def usuario(request):
    respuesta = "Eres " + request.user.username
    return HttpResponse(respuesta)

def busca_pagina(request, identificador):
    login = administrador(request)
    try:
        pag = Pages.objects.get(id = int(identificador))
        respuesta = pag.page
    except Pages.DoesNotExist:
        respuesta = "No existe ese nombre con contenidos en la base de datos"
    template = get_template('plantilla_base.html')
    return HttpResponse(template.render(Context({'texto': respuesta})))

def muestra_todo(request):
    login = administrador(request)
    if login:
        template = get_template('logueado.html')
        usuario = request.user.username
    else:
        usuario = ""
        template = get_template('nologueado.html')
    lista = Pages.objects.all()
    respuesta = "<ol>"
    for pag in lista:
        respuesta += '<li><a href="' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(template.render(Context({'usuario':usuario, 'contenidos':respuesta})))

@csrf_exempt
def nueva_pagina(request):
    logueado = administrador(request)
    if logueado:
        if request.method == "GET":
            # muestro el formulario
            template = get_template('formulario.html')
            return HttpResponse(template.render(Context({})))

        elif request.method == "POST":
            nombre = request.POST['nombre']
            print "este es el nombre " + str(nombre)
            cont = request.POST['contenido']
            print "este es el contenido " + str(cont)
            nueva_pag = Pages(name = str(nombre), page = str(cont))
            nueva_pag.save()
            template = get_template('plantilla_base.html')
            texto = "Pagina anadida correctamente"
        return HttpResponse(template.render(Context({'texto': texto})))
    else:
        template = get_template('plantilla_base.html')
        texto = "Para realizar cambios primero debes hacer login"
        return HttpResponse(template.render(Context({'texto': texto})))
