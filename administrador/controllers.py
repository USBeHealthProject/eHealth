from administrador.models import *
from paciente.models import *
from medico.models import *
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.db.models import F

def register_user(form):
    # Almacenamos el usuario
    save_user = form.save()
    # Agregamos al usuario al grupo de acuerdo al rol
    user = User.objects.get(username=save_user.username)
    usuario = Usuario(user=user, ci=form.cleaned_data['ci'])
    usuario.save()
    group = Group.objects.get(name=form.cleaned_data['rol'])
    user.groups.add(group)
    if form.cleaned_data['rol'] == 'paciente':
        perfil = PerfilPaciente()
        perfil.save()
        paciente = Paciente(cedula=usuario.ci, usuario=usuario,
                            first_name=user.first_name,
                            last_name=user.last_name,
                            perfil=perfil)
        paciente.save()
    elif form.cleaned_data['rol'] == 'medico':
        medico = Medico(cedula=usuario.ci, usuario=usuario,
                        first_name=user.first_name,
                        last_name=user.last_name)
        medico.save()
    return user


def modificar_usuario(usuario_id, username, first_name,
                      last_name, email, rol):
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
        user = User.objects.get(pk=usuario.user.pk)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        group = Group.objects.get(name=rol)
        user.groups.remove(usuario.user.groups.all()[0])
        user.groups.add(group)
        usuario.save()
        user.save()
        return True
    except:
        return False


def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    user = User.objects.get(pk=usuario.user.pk)
    usuario.delete()
    user.delete()
    return HttpResponseRedirect(reverse_lazy(
        'historias_clinicas'))


def agregar_rol(request, name):
    print request.GET
    group = Group(name=name)
    group.save()
    data = {'role': name}
    return HttpResponse(json.dumps(data), status=200,
                        content_type='application/json')


def modificar_rol(request, name, id):
    print name
    group = Group(pk=id)
    group.name = name
    group.save()
    data = {'role': name}
    return HttpResponse(json.dumps(data), status=200,
                        content_type='application/json')


def eliminar_rol(request, id):
    group = Group.objects.get(pk=id)
    group.delete()
    data = {'status': "BIEN"}
    return HttpResponse(json.dumps(data), status=200,
                        content_type='application/json')


def eliminar_institucion(request, name):
    institucion = Institucion.objects.get(pk=name)
    institucion.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_instituciones'))


def eliminar_especialidad(request, name):
    especialidad = Especialidad.objects.get(pk=name)
    especialidad.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_especialidades'))


def eliminar_pregunta(request, pk):
    pregunta = Pregunta.objects.get(pk=pk)
    preguntas_respuestas = PreguntaRespuesta.objects.filter(pregunta__pk=pk)
    especialidad = Especialidad.objects.get(pk=pregunta.especialidad.pk)
    for preg_res in preguntas_respuestas:
        preg_res.pregunta = None
        preg_res.save()
    pregunta.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_preguntas', kwargs={'pk': especialidad.pk}))


def modificar_pregunta(request, pk):
    pregunta = Pregunta.objects.get(pk=pk)
    pregunta.obligatoria = not pregunta.obligatoria
    pregunta.save()
    return HttpResponse(status=200)


def crear_pregunta(pregunta, pk):
    try:
        especialidad = Especialidad.objects.get(pk=pk)
        pregunta = Pregunta(pregunta=pregunta,
                            especialidad=especialidad)
        pregunta.save()
        return True
    except:
        return False


def ordenar_preguntas(request):
    pks = request.POST.getlist('pk')
    for pk in pks:
        posicion = request.POST['posicion_' + pk]
        pregunta = Pregunta.objects.get(pk=pk)
        pregunta.posicion = posicion
        pregunta.save()
    especialidad = Especialidad.objects.get(pk=pregunta.especialidad.pk)
    return HttpResponseRedirect(reverse_lazy(
        'ver_preguntas', kwargs={'pk': especialidad.pk}))
