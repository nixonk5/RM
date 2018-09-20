
from django.conf.urls import url
from .views import (
	PortadaTemplateView,
	)

app_name = 'inicio'

urlpatterns = [
    url(r'^', PortadaTemplateView.as_view(), name='portada'),
]
