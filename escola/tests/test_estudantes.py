from django.contrib.auth.models import User
from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer
from validate_docbr import CPF



class EstudantesTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.user)
        self.estudante_1 = Estudante.objects.create(
            nome='Teste',
            email='teste1@gmail.com',
            cpf='09542780036',
            data_nascimento='2024-11-15',
            num_celular='51 88888-0000'
        )
        self.estudante_2 = Estudante.objects.create(
            nome='TesteDois',
            email='teste2@gmail.com',
            cpf='74693484091',
            data_nascimento='2024-11-15',
            num_celular='51 99945-0000'
        )
    def test_requisicao_get_list_estudantes_200_OK(self):
        """Teste de requisação GET para rota de estudantes"""

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_estudantes_id(self):
        """Teste de requisação GET para rota de estudante por ID"""
        
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(id=1)
        dados_serializados = EstudanteSerializer(instance=dados_estudante).data

        self.assertEqual(response.data, dados_serializados)
    
    def test_requisicao_post_criar_estudante_201_OK(self):
        """Teste de requisação POST para criar Estudante"""
        
        cpf = CPF()
        cpf = cpf.generate()

        dados = {
            'nome':'TestePOST',
            'email': 'testePOST@gmail.com',
            'cpf': '45799589009',
            'data_nascimento':'2024-11-14',
            'num_celular': '86 12345-1234'
        }
        response = self.client.post(self.url, dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_put_estudantes_200_OK(self):
        """Teste requisição PUT alterar Estudante"""
        
                
        dados = {
            'nome': "Put",
            "email": "testeput@gmail.com",
            "cpf": "40419894004",
            "data_nascimento": "2023-12-15",
            "num_celular": "86 12445-1234"
        }

        response = self.client.put(self.url + '1/', dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_estudantes_204_NO_CONTENT(self):
        """Teste requisição DELETE apagar Estudante"""

        response = self.client.delete(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        