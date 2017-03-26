# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0008_auto_20170314_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 17, 55, 25, 472587, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='historiadetriaje',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 17, 55, 25, 471485, tzinfo=utc)),
        ),
    ]
