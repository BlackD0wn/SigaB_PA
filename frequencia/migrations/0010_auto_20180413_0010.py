# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0009_auto_20180413_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='alunos',
            field=models.ManyToManyField(to='frequencia.Aluno'),
        ),
    ]
