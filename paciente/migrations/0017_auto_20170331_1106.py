# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0016_auto_20170331_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 31, 15, 6, 54, 366523, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historiadetriaje',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 31, 15, 6, 54, 365472, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='pregunta',
            field=models.TextField(),
        ),
    ]
