# serializers

from rest_framework import serializers

from .models import *


class TUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'password')
    