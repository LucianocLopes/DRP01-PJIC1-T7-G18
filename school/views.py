from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import School

from .forms import SchoolForm


class SchoolBaseView(PermissionRequiredMixin, View):
    model = School
    templatename = 'school/school_list.html'
    fields = '__all__'
    success_url = reverse_lazy('all')


class SchoolListView(SchoolBaseView, ListView):
    "list view"
    permission_required = 'school.view_school'


class SchoolDetailView(SchoolBaseView, DetailView):
    'detailview'
    form = SchoolForm
    permission_required = 'school.change_school'


class SchoolCreateView(SchoolBaseView, CreateView):
    'createview'
    form = SchoolForm
    permission_required = 'school.add_school'


class SchoolUpdateView(SchoolBaseView, UpdateView):
    'updadeview'
    form = SchoolForm
    permission_required = 'school.change_school'


class SchoolDeleteView(SchoolBaseView, DeleteView):
    'deleteview'
    permission_required = 'school.delete_school'
