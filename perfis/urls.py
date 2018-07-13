from django.conf.urls import patterns, include, url
from django.contrib import admin
from perfis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^perfil/(?P<perfil_id>[0-9]+)$', views.exibir, name='exibir'),
    url(r'^perfil/(?P<perfil_id>[0-9]+)/convidar$', views.convidar, name='convidar')
)
