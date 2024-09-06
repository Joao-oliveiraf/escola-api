
from rest_framework.views import APIView
from rest_framework import generics, status, viewsets, filters
from .serializers import EstudanteSerializer,CursosSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from .models import Estudante,Cursos, Matricula
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

    
class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nivel_do_curso', 'descricao']
    search_fields = ['codigo', 'descricao', 'nivel_do_curso']

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['periodo', 'descricao']
    search_fields = ['codigo', 'descricao', 'nivel_do_curso']

class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset =  Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer
    
class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset =  Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer