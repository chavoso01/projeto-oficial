from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^listar_salas/$', views.listar_salas, name='listar_salas'),
	url(r'^listar_materiais/$', views.listar_materiais, name='listar_materiais'),
	url(r'^cadastrar_salas/$', views.cadastrar_salas, name='cadastrar_salas'), 
	url(r'^cadastrar_materiais/$', views.cadastrar_materiais, name='cadastrar_materiais'), 
	url(r'^$', views.inicio, name='inicio'), 
]