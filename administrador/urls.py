from django.conf.urls import url, patterns
from administrador.views import *

urlpatterns = patterns(
    '',
    url(
        r'^$',
        'administrador.views.user_login',
        name='index'
    ),
    url(
        r'^register/$',
        Register.as_view(),
        name='register'
    ),
    url(
        r'^login/$',
        'administrador.views.user_login',
        name='login'
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/'
        },
        name='logout'),
    url(
        r'^success/$',
        Success.as_view(),
        name='success'
    ),
    url(
        r'^home/$',
        Home.as_view(),
        name='home'
    ),
    url(
        r'^inbox/$',
        Inbox.as_view(),
        name='inbox'
    ),
    url(
        r'^ver-usuarios/$',
        VerUsuarios.as_view(),
        name='ver_usuarios'
    ),
    url(
        r'^modificar-usuario/(?P<pk>\w+)$',
        ModificarUsuario.as_view(),
        name='modificar_usuario'
    ),
    url(
        r'^eliminar-usuario/(?P<id>\w+)$',
        'administrador.controllers.eliminar_usuario',
        name='eliminar_usuario'
    ),
)
