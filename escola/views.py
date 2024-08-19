
from rest_framework.views import APIView
from rest_framework import generics, status, viewsets
from .serializers import EstudanteSerializer,CursosSerializer, MatriculaSerializer
from .models import Estudante,Cursos, Matricula

    
class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
