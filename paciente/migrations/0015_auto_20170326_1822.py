# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0014_auto_20170326_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 22, 52, 47, 196682, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historiadetriaje',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 22, 52, 47, 195130, tzinfo=utc)),
        ),
    ]
