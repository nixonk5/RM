
from django.conf.urls import url
from .views import (
	PortadaTemplateView,
	CursosTemplateView,
	)

app_name = 'inicio'

urlpatterns = [
    url(r'^$', PortadaTemplateView.as_view(), name='portada'),
    url(r'^cursos/$', CursosTemplateView.as_view(), name='cursos'),
]
