from django.test import TestCase
from escola.models import Estudante,Cursos,Matricula
from escola.serializers import EstudanteSerializer, CursosSerializer, MatriculaSerializer
from validate_docbr import CPF

class SerializerEstudanteTestCase(TestCase):

    cpf_gerado = CPF().generate

    def setUp(self):
        
        self.estudante = Estudante(
                nome = 'Teste de Modelo',
                email = 'teste@gmail.com',
                cpf = '68195899056',
                data_nascimento = '2023-08-15',
                num_celular = '51 95487-4587'
        )
        self.serialized_estudante = EstudanteSerializer(instance=self.estudante)
    
    def test_verifica_campos_serializados(self):
        dados = self.serialized_estudante.data # Return dict() of object
        campos = ('id','nome', 'email', 'cpf', 'data_nascimento', 'num_celular')
        self.assertEqual(
            set(dados.keys()),
            set(campos)
        )
    def test_verifica_valores_serializados(self):

        dados = self.serialized_estudante.data # Return dict() of object
        valores_serializados = [i for i in dados.values() if not i is None] # Loop the dict for values, skip 'id' because it's not defined above, therefore is None
        valores_atribuidos = ['Teste de Modelo','teste@gmail.com','68195899056','2023-08-15','51 95487-4587']

        self.assertEqual(set(valores_serializados), set(valores_atribuidos))
        
class SerializerCursosTestCase(TestCase):
    def setUp(self):
        self.curso = Cursos(
            codigo='TC01',
            descricao='Curso TestCase',
            nivel='B'
        )
        self.serialized_curso = CursosSerializer(instance=self.curso)

    def test_verifica_campos_serializados(self):

        dados = self.serialized_curso.data # Dicionario
        # campos = ('codigo', 'descricao','nivel', 'id')
        campos = [field.name for field in Cursos._meta.get_fields() if field.name != 'curso']

        self.assertEqual(set(dados.keys()), set(campos))
    
    def test_verifica_valores_serializados(self):
        
        dados = self.serialized_curso.data
        del dados['id']
        valores = [self.curso.codigo, self.curso.descricao, self.curso.nivel]


        self.assertEqual(
            set(dados.values()),
            set(valores)
        )


class SerializerMatriculaTestCase(TestCase):
    
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'teste@gmail.com',
            cpf = '68195899056',
            data_nascimento = '2023-08-15',
            num_celular = '51 95487-4587'
        )
        self.curso = Cursos.objects.create(
            codigo='KT01',
            descricao='Kotlin 01',
            nivel='A'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='N'
        )
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)
    
    def test_verifica_campos_serializados(self):
        # Matricula Serializada Fields vs Matricula Model Criada Fields

        dados = self.serializer_matricula.data # Return dict
        campos = ('id', 'estudante', 'curso', 'periodo')

        self.assertEqual(dados.keys(), set(campos))

    def test_verifica_valores_serializados(self):
        # Matricula Serializada values vs Matricula.object Value
        dados = self.serializer_matricula.data
        valores = (self.curso.id, self.estudante.id, 'N', self.matricula.id)

        self.assertEqual(set(dados.values()), set(valores))
