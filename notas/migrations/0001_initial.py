# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 00:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frequencia', '0011_auto_20180418_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valorNota', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frequencia.Aluno')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frequencia.Materia')),
            ],
        ),
    ]
