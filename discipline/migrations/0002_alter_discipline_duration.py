# Generated by Django 5.0.3 on 2024-05-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discipline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='duration',
            field=models.IntegerField(verbose_name='Duração (hrs/semana)'),
        ),
    ]