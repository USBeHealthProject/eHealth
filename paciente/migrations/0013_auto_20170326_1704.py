# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0012_auto_20170326_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 21, 4, 5, 758644, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historiadetriaje',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 21, 4, 5, 757588, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='perfilpaciente',
            name='numero_telefono',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfilpaciente',
            name='telefono_emergencia',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
