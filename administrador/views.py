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


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(
            Index, self).get_context_data(**kwargs)
        return context


class Register(CreateView):
    template_name = 'register.html'
    form_class = UsuarioForm

    def get_context_data(self, **kwargs):
        context = super(
            Register, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Registramos al usuario
            register_user(form)
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            return render_to_response('register.html',
                                      {'form': form},
                                      context_instance=RequestContext(
                                          request))


def authenticate_user(username=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(email=username)
            if user is not None:
                return user
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
                if user is not None:
                    return user
            except User.DoesNotExist:
                return None


def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(
            reverse_lazy('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_auth = authenticate_user(username, password)
            if user_auth is not None:
                if user_auth.is_active:
                    user = authenticate(username=user_auth.username,
                                        password=password)
                    if user:
                        login(request, user)
                        return HttpResponseRedirect(
                            reverse_lazy('home'))
                    else:
                        form.add_error(
                            None, "Tu correo o contraseña no son correctos")
                else:
                    form.add_error(None, "Aún no has confirmado tu correo.")
                    user = None
            else:
                form.add_error(
                    None, "Tu correo o contraseña no son correctos")
        else:
            context = {'form': form}
            return render_to_response('index.html', context,
                                      context_instance=RequestContext(request))

    else:
        form = LoginForm()
    context = {'form': form, 'host': request.get_host()}
    return render_to_response('index.html', context,
                              context_instance=RequestContext(request))


class Success(TemplateView):
    template_name = 'success.html'


class Home(TemplateView):
    template_name = 'home.html'


class Inbox(TemplateView):
    template_name = 'administrador/inbox.html'


class VerUsuarios(TemplateView):
    template_name = 'administrador/ver_usuarios.html'

    def get_context_data(self, **kwargs):
        context = super(
            VerUsuarios, self).get_context_data(**kwargs)

        usuarios = Usuario.objects.all()
        context['usuarios'] = usuarios
        return context


class ModificarUsuario(CreateView):
    template_name = 'administrador/modificar_usuario.html'
    form_class = ModificarUsuarioForm

    def get_context_data(self, **kwargs):
        context = super(
            ModificarUsuario, self).get_context_data(**kwargs)
        usuario = Usuario.objects.get(pk=self.kwargs['pk'])
        form = UsuarioForm(
                    initial={'username': usuario.user.username,
                             'first_name': usuario.user.first_name,
                             'last_name': usuario.user.last_name,
                             'email': usuario.user.email,
                             'rol': usuario.user.groups.all()[0],
                             }
                )

        context['form'] = form
        context['usuario'] = usuario

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = ModificarUsuarioForm(request.POST)
        form.fields['passw'].required = False
        form.fields['ci'].required = False
        if form.is_valid():
            usuario_id = kwargs['pk']
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            rol = request.POST['rol']
            value = modificar_usuario(usuario_id, username,
                                      first_name, last_name,
                                      email, rol)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'ver_usuarios'))
            else:
                return render_to_response('administrador/modificar_usuario.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('administrador/modificar_usuario.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))


class VerRoles(TemplateView):
    template_name = 'administrador/ver_roles.html'

    def get_context_data(self, **kwargs):
        context = super(
            VerRoles, self).get_context_data(**kwargs)

        roles = Group.objects.all()
        context['roles'] = roles
        return context


class VerInstituciones(TemplateView):
    template_name = 'administrador/ver_instituciones.html'

    def get_context_data(self, **kwargs):
        context = super(
            VerInstituciones, self).get_context_data(**kwargs)

        instituciones = Institucion.objects.all()
        context['instituciones'] = instituciones
        return context


class AgregarInstitucion(CreateView):
    template_name = 'administrador/crear_institucion.html'
    form_class = InstitucionForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarInstitucion, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('ver_instituciones'))
        else:
            return render_to_response(
                'administrador/crear_institucion.html', {'form': form},
                context_instance=RequestContext(request))


class ModificarInstitucion(UpdateView):
    template_name = 'administrador/crear_institucion.html'
    form_class = InstitucionForm
    success_url = reverse_lazy('ver_instituciones')

    def get_queryset(self):
        return Institucion.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(
            ModificarInstitucion, self).get_context_data(**kwargs)
        institucion = Institucion.objects.get(pk=self.kwargs['pk'])
        form = InstitucionForm(initial={'name': institucion.name,
                                        'address': institucion.address})
        context['institucion'] = institucion
        context['form'] = form
        context['title'] = 'Modificar'

        return context


class VerEspecialidades(TemplateView):
    template_name = 'administrador/ver_especialidades.html'

    def get_context_data(self, **kwargs):
        context = super(
            VerEspecialidades, self).get_context_data(**kwargs)

        especialidad = Especialidad.objects.all()
        context['especialidades'] = especialidad
        return context


class AgregarEspecialidad(CreateView):
    template_name = 'administrador/crear_especialidad.html'
    form_class = EspecialidadForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarEspecialidad, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('ver_especialidades'))
        else:
            return render_to_response(
                'administrador/crear_especialidad.html', {'form': form},
                context_instance=RequestContext(request))


class GestionarHistorias(TemplateView):
    template_name = 'administrador/gestionar_historias.html'

    def get_context_data(self, **kwargs):
        context = super(
            GestionarHistorias, self).get_context_data(**kwargs)

        especialidades = Especialidad.objects.all()

        context['especialidades'] = especialidades

        return context


class VerPreguntas(TemplateView):
    template_name = 'administrador/ver_preguntas.html'

    def get_context_data(self, **kwargs):
        context = super(
            VerPreguntas, self).get_context_data(**kwargs)
        preguntas = Pregunta.objects.filter(especialidad__pk=self.kwargs['pk'])
        especialidad = Especialidad.objects.get(pk=self.kwargs['pk'])
        context['preguntas'] = preguntas
        context['especialidad'] = especialidad

        return context


class CrearPregunta(CreateView):
    template_name = 'administrador/modificar_pregunta.html'
    form_class = PreguntasForm

    def get_context_data(self, **kwargs):
        context = super(
            CrearPregunta, self).get_context_data(**kwargs)

        form = PreguntasForm()

        context['form'] = form
        context['title'] = 'Crear'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        result = crear_pregunta(request.POST['pregunta'], kwargs['pk'])
        if result is True:
            return HttpResponseRedirect(reverse_lazy('ver_preguntas', kwargs={'pk': kwargs['pk']}))
        else:
            return render_to_response(
                'administrador/modificar_pregunta.html',
                context_instance=RequestContext(request))


class ModificarPregunta(UpdateView):
    template_name = 'administrador/modificar_pregunta.html'
    form_class = PreguntasForm
    success_url = reverse_lazy('gestionar_historias')

    def get_queryset(self):
        return Pregunta.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(
            ModificarPregunta, self).get_context_data(**kwargs)

        pregunta = Pregunta.objects.get(pk=self.kwargs['pk'])

        form = PreguntasForm(
            initial={'pregunta': pregunta.pregunta})

        context['form'] = form
        context['title'] = 'Modificar'

        return context
