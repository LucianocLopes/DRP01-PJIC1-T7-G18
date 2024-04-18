# Generated by Django 5.0.3 on 2024-04-18 19:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0003_structschool'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('first_name', models.CharField(max_length=50, verbose_name='Primeiro Nome')),
                ('last_name', models.CharField(max_length=70, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone_ddd', models.CharField(max_length=4, verbose_name='DDD')),
                ('phone_number', models.CharField(max_length=9, verbose_name='Telefone')),
                ('address_zipcode', models.CharField(max_length=9, verbose_name='CEP')),
                ('address', models.CharField(max_length=150, verbose_name='Endereço')),
                ('address_number', models.CharField(max_length=5, verbose_name='Número')),
                ('address_complement', models.CharField(max_length=20, verbose_name='Complemento')),
                ('address_district', models.CharField(max_length=50, verbose_name='Bairro')),
                ('address_city', models.CharField(max_length=70, verbose_name='Cidade')),
                ('address_state', models.CharField(max_length=2, verbose_name='UF')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.school', verbose_name='Escola')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
        ),
    ]
