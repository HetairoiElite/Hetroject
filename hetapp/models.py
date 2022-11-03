from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Tipo_usuario(models.Model):

    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):

    id = models.AutoField(primary_key=True)
    # telefono = models.CharField(max_length=45, blank=True, null=True)
    tipo_usuario = models.ForeignKey(Tipo_usuario,
                                     db_column='tipo_usuario', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "username: " + self.username + " email: " + self.email
