from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import EstudanteSerializer
from .models import Estudante

def estudante(request):
    if request.method == 'GET':
        estudante = {
            'id': '1',
            'nome': 'John'
        }
        return JsonResponse(estudante)
    
class EstudanteView(generics.CreateAPIView):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    

