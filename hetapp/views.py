
from multiprocessing import context
from django.shortcuts import render, HttpResponseRedirect
from .serializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings

from .forms import *


# Create your views here.


def loginForm(request):

    login_form = TUsuarioForm(request.POST or None)

    # clean data

    context = {
        'form': login_form,
    }
    if request.method == 'POST':
        if login_form.is_valid():
            clean_data = login_form.cleaned_data
            try:
                usuario = Usuario.objects.get(
                    username=clean_data.get('username'))
            except Usuario.DoesNotExist:
                login_form.add_error('username', 'El usuario no existe')
                return render(request, 'login.html', context)

            if usuario.check_password(clean_data.get('password')):
                # Crear django session
                request.session['username'] = usuario.username
                request.session['email'] = usuario.email
                request.session['id'] = usuario.id

                request.session['tipo_usuario'] = Tipo_usuario.objects.get(
                    pk=usuario.tipo_usuario).nombre

                print("Session:", request.session['username'])
                print("Session:", request.session['email'])
                print("Session:", request.session['id'])
                print("Session:", request.session['tipo_usuario'])

                return HttpResponseRedirect("/hetapp/hello/")
            else:
                login_form.add_error('password', 'Contraseña incorrecta')
                return render(request, 'login.html', context)

    return render(request, 'login.html', context)


def registro(request):

    registro_form = TUsuarioCreateForm(request.POST or None)

    context = {
        'form': registro_form
    }

    if request.method == 'POST':
        if registro_form.is_valid():
            clean_data = registro_form.cleaned_data

            # ! usuario ya existe
            try:
                usuario = Usuario.objects.get(
                    username=clean_data.get('username'))
                registro_form.add_error('username', 'El usuario ya existe')
                return render(request, 'registro.html', context)
            except Usuario.DoesNotExist:
                pass

            #! correo ya usado

            try:
                usuario = Usuario.objects.get(email=clean_data.get('correo'))
                registro_form.add_error('correo', 'El correo ya esta en uso')
                return render(request, 'registro.html', context)
            except Usuario.DoesNotExist:
                pass

            return HttpResponseRedirect("/hetapp/hello/")

    return render(request, 'registro.html', context=context)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def hello_world(request):

    return Response({'message': 'Hello, world!'})


# @api_view(['POST'])
# @permission_classes([permissions.AllowAny])
# def login(request):
#     try:
#         usuario = TUsuario.objects.get(username=request.data['username'])
#     except TUsuario.DoesNotExist:
#         return Response({'message': 'Ese usuario no existe'})

#     if usuario.check_password(request.data['password']):
#         return Response({'message': 'Login correcto'})
#     else:
#         return Response({'message': 'Contraseña incorrecta'})

def prueba(request):
    messages.info(request, 'Three credits remain in your account.')
    return render(request, 'prueba.html')


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def enviarEmail(request):

    datos = request.data

    titulo = datos['titulo']
    mensaje = datos['mensaje']
    # correo = datos['correo']

    email = EmailMessage(
        titulo,
        mensaje,
        settings.EMAIL_HOST_USER,
        ['jonathan90090@gmail.com']
    )

    email.fail_silently = True
    email.send()

    return Response({'message': 'Email enviado'})
