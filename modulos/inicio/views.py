from django.shortcuts import render
from django.views.generic import (
	TemplateView,
	)

class PortadaTemplateView(TemplateView):
	template_name = "portada.html"
		