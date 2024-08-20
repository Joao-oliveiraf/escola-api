from rest_framework import serializers
from .models import Estudante, Cursos, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ('id','nome', 'email', 'cpf', 'data_nascimento', 'cpf')
class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []
class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]
   
    def get_periodo(self, obj):
        return obj.get_periodo_display()
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante']
