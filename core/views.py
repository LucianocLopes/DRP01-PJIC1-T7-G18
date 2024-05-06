from typing import Any
from django.shortcuts import render
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
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context