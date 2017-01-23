from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User)
    rol = models.CharField(
        max_length=100, default='-',
        choices=[
            ('admin', 'Administrador'),
            ('medico', 'Médico'),
            ('paciente', 'Paciente'),
        ]
    )

    def __str__(self):
        return self.user.username
