from rest_framework import serializers
from .models import Estudante, Cursos

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ('id','nome', 'email', 'cpf', 'data_nascimento', 'cpf')
class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'