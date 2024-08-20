
from rest_framework.views import APIView
from rest_framework import generics, status, viewsets
from .serializers import EstudanteSerializer,CursosSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from .models import Estudante,Cursos, Matricula
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

    
class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

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