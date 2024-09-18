from django.contrib.auth.models import User
from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status
from escola.models import Cursos, Estudante, Matricula
import random



class MatriculasTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.user)
        self.curso_01 = Cursos.objects.create(
            codigo = 'CTC01',
            descricao= 'Curso Teste Case 01',
            nivel='B'
        )
        self.estudante_1 = Estudante.objects.create(
            nome='Teste01',
            email='teste1@gmail.com',
            cpf='12345',
            data_nascimento='2024-11-15',
            num_celular='51 88888-0000'
        )
        self.matricula_01 = Matricula.objects.create(
            estudante=self.estudante_1,
            curso=self.curso_01,
            periodo='M'
        )
    
    def test_requisicao_get_matriculas_list(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_post_criar_curso_201_OK(self):
        """Teste de requisação POST para criar Matricula"""
        dados = {
            'estudante':self.estudante_1.id,
            'curso':self.curso_01.id,
            'periodo':random.choice(['M', 'V', 'N'])
        }
        response = self.client.post(self.url, dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_put_matricula_405(self):
        """Teste de requisição PUT para Matricula"""
        
        response = self.client.put(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_delete_matricula_405(self):
        """Teste requisição DELETE apagar Estudante"""

        response = self.client.delete(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
