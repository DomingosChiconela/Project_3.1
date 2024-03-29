# Generated by Django 4.1.7 on 2023-03-25 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passageiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30, validators=[django.core.validators.EmailValidator(message='email  invalido')])),
                ('endereco', models.CharField(max_length=60, verbose_name='Endereço')),
                ('celular1', models.CharField(max_length=12)),
                ('celular2', models.CharField(blank=True, max_length=12)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Gênero')),
                ('numeroEmer', models.CharField(max_length=12, verbose_name='Numero de Emergência')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
