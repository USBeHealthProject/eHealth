#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from administrador.models import *
from medico.models import *
from paciente.models import *


class PerfilPacienteForm(forms.ModelForm):

    sexo = forms.ChoiceField(
        required=True,
        choices=[
            ('', 'Seleccione su sexo'),
            ('Femenino', 'Femenino'),
            ('Masculino', 'Masculino'),
        ]
    )

    tipo_sangre = forms.ChoiceField(
        required=True,
        choices=[
            ('', 'Seleccione su tipo de sangre'),
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ]
    )

    estado_civil = forms.ChoiceField(
        required=True,
        choices=[
            ('', 'Seleccione su estado civil'),
            ('Soltero', 'Soltero'),
            ('Casado', 'Casado'),
            ('Viudo', 'Viudo'),
            ('Divorciado', 'Divorciado'),
            ('Otro', 'Otro'),
        ]
    )

    class Meta:
        model = PerfilPaciente
        fields = '__all__'


        widgets = {
            'email': forms.TextInput(attrs={'required': 'true'}),
            'first_name': forms.TextInput(attrs={'required': 'true'}),
            'last_name': forms.TextInput(attrs={'required': 'true'})
        }

        labels = {
            'email': 'Correo',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
