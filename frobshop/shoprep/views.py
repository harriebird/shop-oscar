from django.shortcuts import render
# from django.core.urlresolvers import reverse
from django.views.generic import RedirectView, TemplateView
from oscar.core.loading import get_class, get_model
from oscar.apps.catalogue.models import AbstractProduct


# Create your views here.
class IndexView(TemplateView):
    model = AbstractProduct
    template_name = 'templates/home.html'
