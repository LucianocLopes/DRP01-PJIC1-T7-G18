# Generated by Django 5.0.3 on 2024-04-26 00:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('name', models.CharField(max_length=50, verbose_name='Estado')),
                ('abbreviaton', models.CharField(max_length=2, verbose_name='Abreviacao')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('name', models.CharField(max_length=50, verbose_name='Cidade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado', verbose_name='UF')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Lougradouro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('name', models.CharField(max_length=50, verbose_name='Tipo de Lougradouro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Lougradouro',
                'verbose_name_plural': 'Lougradouros',
            },
        ),
        migrations.CreateModel(
            name='AddressBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('zip_code', models.CharField(max_length=8, verbose_name='CEP')),
                ('adrress', models.CharField(max_length=100, verbose_name='Endereço')),
                ('district', models.CharField(max_length=50, verbose_name='Bairro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.cidade', verbose_name='Cidade')),
                ('type_lougradouro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.lougradouro', verbose_name='Tipo de Lougradouro')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]