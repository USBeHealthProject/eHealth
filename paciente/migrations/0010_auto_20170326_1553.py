# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0009_auto_20170326_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilPaciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.CharField(max_length=30, null=True, blank=True)),
                ('altura', models.IntegerField(max_length=30, null=True, blank=True)),
                ('peso', models.IntegerField(max_length=30, null=True, blank=True)),
                ('tipo_sangre', models.CharField(max_length=30, null=True, blank=True)),
                ('diabetico', models.CharField(max_length=30, null=True, blank=True)),
                ('alergias', models.CharField(max_length=30, null=True, blank=True)),
                ('contacto_emergencia', models.CharField(max_length=30, null=True, blank=True)),
                ('telefono_emergencia', models.IntegerField(max_length=30, null=True, blank=True)),
                ('comentarios', models.CharField(max_length=999, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='historia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 19, 53, 23, 407935, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historiadetriaje',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 26, 19, 53, 23, 406736, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='paciente',
            name='perfil',
            field=models.ForeignKey(to='paciente.PerfilPaciente', null=True),
        ),
    ]
