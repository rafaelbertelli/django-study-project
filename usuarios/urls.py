from django.conf.urls import patterns, url
from django.contrib import admin
from views import RegistrarUsuarioView

urlpatterns = patterns('',
    url(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
)
