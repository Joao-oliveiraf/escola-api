from rest_framework import serializers
from .models import Estudante, Cursos, Matricula
from .validators import nome_invalido,num_celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ('id','nome', 'email', 'cpf', 'data_nascimento', 'num_celular')

    def validate_num_celular(self, num_celular):
        if num_celular_invalido(num_celular):
            raise serializers.ValidationError('Número de celular deve seguir o padrão: xx xxxxx-xxxx')
        return num_celular
    
    def validate_nome(self, nome):
         if nome_invalido(nome):
              raise serializers.ValidationError('Nome deve conter apenas letras!')
         return nome
    
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
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ('id','nome', 'email', 'num_celular')