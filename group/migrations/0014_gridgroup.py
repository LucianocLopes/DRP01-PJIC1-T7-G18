# Generated by Django 5.0.6 on 2024-05-14 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0013_rename_identification_group_group_id_and_more'),
        ('teacher', '0002_alter_teacher_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='GridGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_week', models.CharField(choices=[('Sunday', 'Domingo'), ('Monday', 'Segunda-Feira'), ('tuesday', 'Terca-Feira'), ('Wednesday', 'Quarta-Feira'), ('Thursday', 'Quinta-Feira'), ('Friday', 'Sexta-Feira'), ('Saturday', 'Sábado')], max_length=15, verbose_name='Dia da Semana')),
                ('time_start', models.TimeField(verbose_name='Horario inicial')),
                ('duration_lesson', models.PositiveIntegerField(default=60, help_text='Informe um intervalo em minutos', verbose_name='Duração (minutos)')),
                ('description', models.CharField(max_length=254, verbose_name='Descrição')),
                ('grup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.group', verbose_name='Classe')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher', verbose_name='Professor')),
            ],
            options={
                'verbose_name': 'GripGroup',
                'verbose_name_plural': 'GripGroups',
            },
        ),
    ]