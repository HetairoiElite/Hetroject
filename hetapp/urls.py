# urls de hetapp

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginForm, name='login'),
    path('hello/', views.hello_world, name='hello'),
    # path('login_logic/', views.login, name='login_logic'),
    path('registro/', views.registro, name='registro'),
    path('enviar_correo/', views.enviarEmail, name='enviar_correo'),
    path('prueba/', views.prueba, name='prueba'),
]
