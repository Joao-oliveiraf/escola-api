from django.db import models
from localflavor.br.models import BRCPFField
from django.core.validators import MinLengthValidator

class Estudante(models.Model):
    nome = models.CharField(
        max_length=250,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        blank=False,
        null=False,
        unique=True,
    )
    cpf  = BRCPFField(
        unique=True,
        
    )
    data_nascimento = models.DateField(
        blank=False,
        null=False,
    )
    num_celular = models.CharField(
        max_length=14,
        unique=True,
        blank=False,
        null=False
    )

    def __str__(self) -> str:
        return self.nome
class Cursos(models.Model):
    ESCOLHAS = [
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    ]
    codigo = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        validators=[MinLengthValidator(3)]
    )
    descricao = models.TextField(
        max_length=255,
        blank=False,
        null=False,
    )
    nivel = models.CharField(
        max_length=1,
        choices=ESCOLHAS,
        blank=False,
        default='B',
    )
    def __str__(self) -> str:
        return self.descricao
class Matricula(models.Model):
    CHOICES = [
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    ]
    estudante = models.ForeignKey(
        Estudante,
        on_delete=models.CASCADE,
        related_name='estudante',
    )
    curso = models.ForeignKey(
        Cursos,
        on_delete=models.CASCADE,
        related_name='curso',
    )
    periodo = models.CharField(
        max_length=1,
        blank=False,
        null=False,
        choices=CHOICES,
        default='M'
    )