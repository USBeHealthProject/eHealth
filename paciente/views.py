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
