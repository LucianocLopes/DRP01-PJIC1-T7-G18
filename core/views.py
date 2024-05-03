from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from school.models import School

class IndexView(LoginRequiredMixin, TemplateView):    
    template_name = "core/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context