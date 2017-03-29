from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.core.urlresolvers import reverse
from medico.models import *


class PerfilPaciente(models.Model):
    fecha_nacimiento = models.DateField(null=True)
    estado_civil = models.CharField(max_length=30, blank=True, null=True)
    numero_telefono = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=30, blank=True, null=True)
    sexo = models.CharField(max_length=30, blank=True, null=True)
    altura = models.DecimalField(max_digits=20, decimal_places=2,
                                   default=0.00, blank=True, null=True)
    peso = models.DecimalField(max_digits=20, decimal_places=2,
                                   default=0.00, blank=True, null=True)
    tipo_sangre = models.CharField(max_length=30, blank=True, null=True)
    diabetico = models.CharField(max_length=30, blank=True, null=True)
    alergias = models.CharField(max_length=30, blank=True, null=True)
    contacto_emergencia = models.CharField(max_length=30, blank=True,
                                           null=True)
    telefono_emergencia = models.CharField(max_length=30, blank=True, null=True)
    comentarios = models.CharField(max_length=999, blank=True, null=True)


class Paciente(models.Model):
    ESTADOS_CIVILES = (
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
    )
    cedula = models.IntegerField(primary_key=True,
                                 validators=[MaxValueValidator(99999999)])
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=70, blank=True, null=True)
    estado_civil = models.CharField(max_length=7, choices=ESTADOS_CIVILES,
                                    blank=True, null=True)
    ocupacion = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=70, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario,
                                on_delete=models.CASCADE)
    perfil = models.ForeignKey(PerfilPaciente,
                               on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.cedula) + "  " + self.first_name + " " + self.last_name

    def str_busqueda(self):
        return 'Paciente: (CI ' + str(self.cedula) + ")  " + self.first_name + " " + self.last_name


class Historiadetriaje(models.Model):
    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico_triaje = models.ForeignKey('medico.Medico',
                                      on_delete=models.CASCADE)
    antecedentes_personales = models.CharField(max_length=500)
    antecedentes_familiares = models.CharField(max_length=500)
    motivo_consulta = models.CharField(max_length=200)
    enfermedad_actual = models.CharField(max_length=200)
    peso = models.DecimalField(max_digits=5,decimal_places=2)
    talla = models.DecimalField(max_digits=5,decimal_places=2)
    signos_vitales = models.CharField(max_length=200)
    piel = models.CharField(max_length=200)
    ojos = models.CharField(max_length=200)
    fosas_nasales = models.CharField(max_length=200)
    conductos_auditivos = models.CharField(max_length=200)
    cavidad_oral = models.CharField(max_length=200)
    cuello = models.CharField(max_length=200)
    columna = models.CharField(max_length=200)
    torax = models.CharField(max_length=200)
    abdomen = models.CharField(max_length=200)
    extremidades = models.CharField(max_length=200)
    genitales = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.localtime(timezone.now()))


class Historia(models.Model):
    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico = models.ForeignKey('medico.Medico',
                               on_delete=models.CASCADE)
    especialidad = models.ForeignKey('medico.Especialidad',
                                     on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.localtime(timezone.now()))

    def str_busqueda(self):
        return 'Historia ' + str(self.especialidad) + ': (' + self.fecha.strftime("%d/%m/%y") + ') ' + str(self.paciente)

    def get_absolute_url(self):
        return reverse('pdf_especialidad', args=[self.pk])


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200)
    especialidad = models.ForeignKey('medico.Especialidad',
                    on_delete=models.CASCADE,
                    null=True)
    obligatoria = models.BooleanField(default=False)
    posicion = models.CharField(max_length=3, null=True)

    def __str__(self):
        return str(self.pregunta)


class PreguntaRespuesta(models.Model):
    historia = models.ForeignKey(Historia,
                                 on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200)
    pregunta = models.ForeignKey(Pregunta,
                                 on_delete=models.CASCADE,
                                 null=True)
    pregunta_historia = models.CharField(max_length=200, null=True)

    def get_absolute_url(self):
        return reverse('ver_historia_especialidad', args=[self.historia.pk])

    def str_busqueda(self):
        return self.historia.str_busqueda()
