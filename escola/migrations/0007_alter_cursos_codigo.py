# Generated by Django 5.1 on 2024-09-04 20:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0006_alter_matricula_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='codigo',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
