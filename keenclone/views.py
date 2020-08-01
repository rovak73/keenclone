from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexPage(TemplateView):

    template_name = "index.html"

