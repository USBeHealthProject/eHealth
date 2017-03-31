# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0015_auto_20170326_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 31, 15, 5, 48, 896845, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historiadetriaje',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 31, 15, 5, 48, 895803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='preguntarespuesta',
            name='respuesta',
            field=models.TextField(),
        ),
    ]
