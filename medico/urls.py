"""medico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from medico.views import *


urlpatterns = [
    url(
        r'^perfil-medico/(?P<id>\w+)$',
        PerfilMedico.as_view(),
        name='perfil_medico'
    ),
    url(
        r'^agregar-estudios/(?P<id>\w+)$',
        AgregarEstudios.as_view(),
        name='agregar_estudios'
    ),
    url(
        r'^modificar-estudios/(?P<id>\w+)$',
        ModificarEstudios.as_view(),
        name='modificar_estudios'
    ),
    url(
        r'^eliminar-estudios/(?P<id>\w+)$',
        'medico.controllers.eliminar_estudios',
        name='eliminar_estudios'
    ),
    url(
        r'^agregar-reconocimientos/(?P<id>\w+)$',
        AgregarReconocimientos.as_view(),
        name='agregar_reconocimientos'
    ),
    url(
        r'^modificar-reconocimientos/(?P<id>\w+)$',
        ModificarReconocimientos.as_view(),
        name='modificar_reconocimientos'
    ),
    url(
        r'^eliminar-reconocimientos/(?P<id>\w+)$',
        'medico.controllers.eliminar_reconocimientos',
        name='eliminar_reconocimientos'
    ),
    url(
        r'^agregar-publicaciones/(?P<id>\w+)$',
        AgregarPublicaciones.as_view(),
        name='agregar_publicaciones'
    ),
    url(
        r'^modificar-publicaciones/(?P<id>\w+)$',
        ModificarPublicaciones.as_view(),
        name='modificar_publicaciones'
    ),
    url(
        r'^eliminar-publicaciones/(?P<id>\w+)$',
        'medico.controllers.eliminar_publicaciones',
        name='eliminar_publicaciones'
    ),
    url(
        r'^agregar-experiencias/(?P<id>\w+)$',
        AgregarExperiencias.as_view(),
        name='agregar_experiencias'
    ),
    url(
        r'^modificar-experiencias/(?P<id>\w+)$',
        ModificarExperiencias.as_view(),
        name='modificar_experiencias'
    ),
    url(
        r'^eliminar-experiencias/(?P<id>\w+)$',
        'medico.controllers.eliminar_experiencias',
        name='eliminar_experiencias'
    ),
    url(
        r'^agregar-habilidades/(?P<id>\w+)$',
        AgregarHabilidades.as_view(),
        name='agregar_habilidades'
    ),
    url(
        r'^modificar-habilidades/(?P<id>\w+)$',
        ModificarHabilidades.as_view(),
        name='modificar_habilidades'
    ),
    url(
        r'^eliminar-habilidades/(?P<id>\w+)$',
        'medico.controllers.eliminar_habilidades',
        name='eliminar_habilidades'
    ),
    url(
        r'^agregar-eventos/(?P<id>\w+)$',
        AgregarEventos.as_view(),
        name='agregar_eventos'
    ),
    url(
        r'^modificar-eventos/(?P<id>\w+)$',
        ModificarEventos.as_view(),
        name='modificar_eventos'
    ),
    url(
        r'^eliminar-eventos/(?P<id>\w+)$',
        'medico.controllers.eliminar_eventos',
        name='eliminar_eventos'
    ),
    url(
        r'^ver-consultas/(?P<id>\w+)$',
        VerConsultas.as_view(),
        name='ver_consultas'
    ),
    url(
        r'^agregar-consulta/$',
        AgregarConsulta.as_view(),
        name='agregar_consulta'
    ),
    url(
        r'^buscar-paciente$',
        BuscarPaciente.as_view(),
        name='buscar_paciente'
    ),
    url(
        r'^buscar-medico$',
        BuscarMedico.as_view(),
        name='buscar_medico'
    ),
    url(
        r'^ver-citas/(?P<id>\w+)$',
        VerCitas.as_view(),
        name='ver_citas'
    ),
    url(
        r'^agregar-cita/(?P<id>\w+)$',
        AgregarCitas.as_view(),
        name='agregar_cita'
    ),
    url(
        r'^modificar-cita/(?P<id>\w+)$',
        ModificarCitas.as_view(),
        name='modificar_cita'
    ),
    url(
        r'^eliminar-cita/(?P<id>\w+)$',
        'medico.controllers.eliminar_citas',
        name='eliminar_cita'
    ),
    url(
        r'^historias/$',
        HistoriasClinicas.as_view(),
        name='historias_clinicas'
    ),
    url(
        r'^historias/new/$',
        HistoriasClinicasCrear.as_view(),
        name='crear_historias_clinicas'
    ),
    url(
        r'^ver-historia-clinica/(?P<pk>\w+)$',
        HistoriasClinicasModificar.as_view(),
        name='ver_historia_clinica'
    ),
    url(
        r'^eliminar-historia_clinica/(?P<id>\w+)$',
        'medico.controllers.eliminar_historia_clinica',
        name='eliminar_historia_clinica'
    ),
    url(
        r'^historias_especialidad$',
        HistoriasEspecialidad.as_view(),
        name='historias_especialidad'
    ),
    url(
        r'^historias_especialidad/new/$',
        HistoriasEspecialidadCrear.as_view(),
        name='crear_historias_especialidad'
    ),
    url(
        r'^ver-historia-especialidad/(?P<pk>\w+)$',
        HistoriasEspecialidadModificar.as_view(),
        name='ver_historia_especialidad'
    ),
    url(
        r'^eliminar-historia-especialidad/(?P<id>\w+)$',
        'medico.controllers.eliminar_historia_especialidad',
        name='eliminar_historia_especialidad'
    ),
    url(
        r'^obtener-preguntas-especialidad/(?P<especialidad>[\w ]+)$',
        'medico.controllers.obtener_preguntas_especialidad',
        name='obtener_preguntas_especialidad'
    ),

    url(r'^pdf/(?P<pk>\w+)$', MyPDFViewTriaje.as_view(), name='pdf_triaje'),
    url(r'^pdfe/(?P<pk>\w+)$', MyPDFViewEspecialidad.as_view(), name='pdf_especialidad'),
]
