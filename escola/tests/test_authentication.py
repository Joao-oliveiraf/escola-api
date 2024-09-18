from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status



class AuthenticateUserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.url = reverse('Estudantes-list')

    def test_user_authenticate_correct(self):
        """Teste para autenticação com credencias corretas"""
        
        user = authenticate(
            username='admin',
            password='admin'
        )
        self.assertTrue((user is not None) and (user.is_authenticated))
    
    def test_user_authenticate__username_incorrect(self):
        """Teste para autenticação com username incorreto"""

        user = authenticate(
            username='admn',
            password='admin'
        )
        self.assertFalse((user is not None) and (user.is_authenticated))
    
    def test_user_authenticate__password_incorrect(self):
        """Teste para autenticação com password incorreta"""

        user = authenticate(
            username='admin',
            password='adn'
        )
        self.assertFalse((user is not None) and (user.is_authenticated))
    
    def test_requisicao_get_autorizada(self):
        """Teste para requisicao get autorizada"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_get__nao_autorizada(self):
        """Teste para requisicao get não autorizada"""
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

