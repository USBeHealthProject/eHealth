# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0011_auto_20170326_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 21, 3, 25, 443015, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historiadetriaje',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 21, 3, 25, 441952, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='perfilpaciente',
            name='altura',
            field=models.DecimalField(default=0.0, null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='perfilpaciente',
            name='numero_telefono',
            field=models.DecimalField(default=0.0, null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='perfilpaciente',
            name='peso',
            field=models.DecimalField(default=0.0, null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='perfilpaciente',
            name='telefono_emergencia',
            field=models.DecimalField(default=0.0, null=True, max_digits=20, decimal_places=2, blank=True),
        ),
    ]
