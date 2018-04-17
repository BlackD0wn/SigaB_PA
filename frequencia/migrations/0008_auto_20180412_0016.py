# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0007_frequencia_presente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='alunos',
        ),
        migrations.AddField(
            model_name='aluno',
            name='materias',
            field=models.ManyToManyField(to='frequencia.Materia'),
        ),
    ]