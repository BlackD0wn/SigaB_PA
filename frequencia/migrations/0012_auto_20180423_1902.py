# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0011_auto_20180418_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frequencia',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='presente',
        ),
        migrations.AddField(
            model_name='frequencia',
            name='presente',
            field=models.ManyToManyField(to='frequencia.Aluno'),
        ),
    ]
