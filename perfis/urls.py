from django.conf.urls import patterns, url
from django.contrib import admin
from perfis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^perfil/(?P<perfil_id>[0-9]+)$', views.exibir, name='exibir'),
    url(r'^perfil/(?P<perfil_id>[0-9]+)/convidar$', views.convidar, name='convidar'),
    url(r'^perfil/(?P<convite_id>[0-9]+)/aceitar$', views.aceitar, name='aceitar'),
    url(r'^perfil/(?P<convite_id>[0-9]+)/deletar$', views.deletar, name='deletar'),
)
