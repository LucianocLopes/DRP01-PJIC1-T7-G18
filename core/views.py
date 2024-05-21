from django.shortcuts import render

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