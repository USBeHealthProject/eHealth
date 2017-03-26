# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0010_auto_20170326_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilpaciente',
            name='direccion',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='perfilpaciente',
            name='estado_civil',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='perfilpaciente',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='perfilpaciente',
            name='numero_telefono',
            field=models.IntegerField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 20, 11, 56, 900450, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historiadetriaje',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 20, 11, 56, 899357, tzinfo=utc)),
        ),
    ]
