from django.test import TestCase
from escola.models import Estudante, Cursos

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_fixtures(self):
        """Teste para verificar o carregamento da fixtures"""

        estudante = Estudante.objects.get(cpf=78499737200)
        curso = Cursos.objects.get(id=1)

        self.assertEqual(estudante.num_celular, '76 96299-7595')
        self.assertEqual(curso.codigo,"CPOO1")        