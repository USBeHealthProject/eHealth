# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('nombre_especialidad', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('cedula', models.IntegerField(serialize=False, primary_key=True, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('sexo', models.CharField(max_length=10)),
                ('estado_civil', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(to='administrador.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('especialidad', models.ForeignKey(to='medico.Especialidad')),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Estudios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('fecha_graduacion', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('institucion', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Eventos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
                ('institucion', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Experiencias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('institucion', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Habilidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Logros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Publicaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('autores', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('revista', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=5)),
                ('volumen', models.CharField(max_length=5)),
                ('fecha', models.DateField()),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
    ]
