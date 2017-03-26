#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import *
from django.views.generic import *
from administrador.forms import *
from administrador.models import *
from administrador.controllers import *
from medico.models import *
from paciente.forms import *


class Perfil(TemplateView):
    template_name = 'paciente/perfil.html'

    def get_context_data(self, **kwargs):
        context = super(
            Perfil, self).get_context_data(**kwargs)
        user = self.request.user
        usuario = Usuario.objects.get(user=user)
        paciente = Paciente.objects.get(usuario__pk=usuario.pk)
        historias = Historia.objects.filter(paciente__pk=paciente.pk)
        perfil = PerfilPaciente.objects.get(pk=paciente.perfil.pk)
        form = PerfilPacienteForm(initial={
                                  'fecha_nacimiento': perfil.fecha_nacimiento,
                                  'estado_civil': perfil.estado_civil,
                                  'numero_telefono': perfil.numero_telefono,
                                  'direccion': perfil.direccion,
                                  'sexo': perfil.sexo,
                                  'altura': perfil.altura,
                                  'peso': perfil.peso,
                                  'tipo:sangre': perfil.tipo_sangre,
                                  'diabetico': perfil.diabetico,
                                  'alergias': perfil.alergias,
                                  'contacto_emergencia': perfil.contacto_emergencia,
                                  'telefono_emergencia': perfil.telefono_emergencia,
                                  'comentarios': perfil.comentarios
                                  })
        context['usuario'] = usuario
        context['historias'] = historias
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        usuario = Usuario.objects.get(user__pk=request.user.pk)
        paciente = Paciente.objects.get(usuario__pk=usuario.pk)
        instancia = PerfilPaciente.objects.get(paciente__pk=paciente.pk)
        form = PerfilPacienteForm(request.POST, instance=instancia)
        print form.errors
        if form.is_valid():
            perfil = form.save()
            perfil.save()
        return HttpResponseRedirect(reverse_lazy('perfil'))


class MisHistorias(TemplateView):
    template_name = 'paciente/mis_historias.html'

    def get_context_data(self, **kwargs):
        context = super(
            MisHistorias, self).get_context_data(**kwargs)
        user = self.request.user
        usuario = Usuario.objects.get(user=user)
        paciente = Paciente.objects.get(usuario__pk=usuario.pk)
        historias = Historia.objects.filter(paciente__pk=paciente.pk)
        context['historias'] = historias
        return context


class MiHistoria(TemplateView):
    template_name = 'paciente/mi_historia.html'

    def get_context_data(self, **kwargs):
        context = super(
            MiHistoria, self).get_context_data(**kwargs)
        preguntas = PreguntaRespuesta.objects.filter(historia__pk=kwargs['pk'])
        historia = Historia.objects.get(pk=kwargs['pk'])
        context['preguntas'] = preguntas
        context['historia'] = historia
        return context
