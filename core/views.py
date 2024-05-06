from typing import Any
from django.shortcuts import render
<<<<<<< HEAD

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from school.models import School, AddressSchool, PhoneSchool

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['school'] = School.objects.select_related().all().first()
        context['addresses'] = AddressSchool.objects.select_related().all()
        context['phones'] = PhoneSchool.objects.select_related().all()
        return context


def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)


def server_error(request):
    return render(request, 'core/500.html', status=500)
=======
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from school.models import School
from django.shortcuts import render



def pagina_nao_encontrada(request, exception):
    return render(request, 'core/404.html', status=404)


def erro_servidor(request):
    return render(request, 'core/500.html', status=500)


class IndexView(LoginRequiredMixin, TemplateView):    
    template_name = "core/index.html"
<<<<<<< HEAD
>>>>>>> a8c0174 (include core app and configs)
=======
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context
>>>>>>> d22ecf1 (correctons apps school. schedule, core)
