from django.contrib.auth.models import User
from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status
from escola.models import Cursos
from escola.serializers import CursosSerializer
import random



class CursosTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.user)
        self.curso_01 = Cursos.objects.create(
            codigo = 'CTC01',
            descricao= 'Curso Teste Case 01',
            nivel='B'
        )
        self.curso_02 = Cursos.objects.create(
            codigo = 'CTC02',
            descricao= 'Curso Teste Case 02',
            nivel='z'
        )
    def test_requisicao_get_cursos_list(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_get_cursos_id(self):
        """Teste de requisação GET para rota de cursos por ID"""
        
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Cursos.objects.get(id=1)
        dados_serializados = CursosSerializer(instance=dados_curso).data

        self.assertEqual(response.data, dados_serializados)
    
    def test_requisicao_post_criar_curso_201_CREATED(self):
        """Teste de requisação POST para criar Curso"""
        
        dados = {
            'codigo':'CT01',
            'descricao':'Teste Curso 201 created',
            'nivel': random.choices(['B', 'I', 'A'])
        }
        response = self.client.post(self.url, dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_put_cursos_200_OK(self):
        """Teste requisição PUT alterar nome Estudante"""
        
        dados = {
            'codigo':'PTC01',
            'descricao':'PUT 01',
            'nivel':'B'
        }
        response = self.client.put(self.url + '1/', dados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_delete_cursos_204_NO_CONTENT(self):
        """Teste requisição DELETE apagar Estudante"""

        response = self.client.delete(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



        