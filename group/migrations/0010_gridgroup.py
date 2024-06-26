# Generated by Django 5.0.6 on 2024-05-11 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0009_delete_gridgroup'),
        ('school', '0007_schoolyear'),
    ]

    operations = [
        migrations.CreateModel(
            name='GridGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField(verbose_name='Horario inicial')),
                ('duration_lesson', models.PositiveIntegerField(default=60, help_text='Informe um intervalo em minutos', verbose_name='Duração (minutos)')),
                ('number_classes', models.PositiveIntegerField(default=5, help_text='Informe de aulas no dia', verbose_name='Quantidade de Aulas')),
                ('interval_start', models.DateTimeField(verbose_name='Inicio do Intervalo')),
                ('duration_interval', models.PositiveIntegerField(default=30, help_text='Informe um intervalo em minutos', verbose_name='Duração do intervalo')),
                ('grup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.group', verbose_name='Classe')),
                ('schoolyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schoolyear', verbose_name='Ano Letivo')),
            ],
            options={
                'verbose_name': 'GripGroup',
                'verbose_name_plural': 'GripGroups',
            },
        ),
    ]
