from django.test import TestCase
from escola.models import Estudante,Cursos, Matricula
from validate_docbr import CPF
import random

class ModelEstudante(TestCase):

    # def test_falha(self):
    #     return self.fail('Teste falhou :(')

    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'teste@gmail.com',
            cpf = CPF().generate,
            data_nascimento = '2023-08-15',
            num_celular = '51 95487-4587'
        )
    def test_verificar_atributos(self):
        """
        Teste para verificar os atributos do modelo Estudante
        """
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'teste@gmail.com')
        self.assertTrue(self.estudante.cpf)
        self.assertEqual(self.estudante.data_nascimento, '2023-08-15')
        self.assertEqual(self.estudante.num_celular, '51 95487-4587')
        
        

class ModelCursosTestCase(TestCase):

    def setUp(self):
        self.curso = Cursos.objects.create(
            codigo='KT01',
            descricao='Kotlin 01',
            nivel=random.choice(['B', 'I', 'A'])
        )
    
    def test_curso_atributos(self):

        self.assertEqual(self.curso.codigo, 'KT01')
        self.assertEqual(self.curso.descricao, 'Kotlin 01')
        self.assertIn(self.curso.nivel, ['B', 'I', 'A'])

class ModelMatriculaTesteCase(TestCase):

    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'teste@gmail.com',
            cpf = CPF().generate,
            data_nascimento = '2023-08-15',
            num_celular = '51 95487-4587'
        )
        self.curso = Cursos.objects.create(
            codigo='KT01',
            descricao='Kotlin 01',
            nivel=random.choice(['B', 'I', 'A'])
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo=random.choice(['M','V','N'])
        )
    def test_matricula_atributos(self):
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertIn(self.matricula.periodo, ['M','V','N'])
