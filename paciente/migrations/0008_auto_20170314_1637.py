# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0007_auto_20170308_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='posicion',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='preguntarespuesta',
            name='respuesta',
            field=models.CharField(max_length=200),
        ),
    ]
