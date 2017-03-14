# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0006_pregunta_obligatoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntarespuesta',
            name='respuesta',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(regex=b'/^[a-z]+[0-9_\\/\\s,.-]+$/i', message=b'La pregunta no debe ser vacia')]),
        ),
    ]
