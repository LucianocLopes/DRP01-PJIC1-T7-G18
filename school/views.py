from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import School, StructSchool

from .forms import SchoolForm, StructSchoolForm


class SchoolBaseView(PermissionRequiredMixin, View):
    model = School
    templatename = 'school/school_list.html'
    success_url = reverse_lazy('school_all')


class SchoolListView(SchoolBaseView, ListView):
    "list view"
    permission_required = 'school.view_school'


class SchoolDetailView(SchoolBaseView, DetailView):
    'detailview'
    form_class = SchoolForm
    permission_required = 'school.change_school'


class SchoolCreateView(SchoolBaseView, CreateView):
    'createview'
    form_class = SchoolForm
    permission_required = 'school.add_school'


class SchoolUpdateView(SchoolBaseView, UpdateView):
    'updadeview'
    form_class = SchoolForm
    permission_required = 'school.change_school'


class SchoolDeleteView(SchoolBaseView, DeleteView):
    'deleteview'
    permission_required = 'school.delete_school'


class StructBaseView(PermissionRequiredMixin, View):
    model = StructSchool
    templatename = 'school/struct/structschool_list.html'
    success_url = reverse_lazy('struct_all')


class StructListView(StructBaseView, ListView):
    "list view"
    templatename = 'school/struct/structschool_list.html'
    permission_required = 'structschool.view_structschool'


class StructDetailView(StructBaseView, DetailView):
    'detailview'
    templatename = 'school/struct/structschool_detail.html'
    form_class = StructSchoolForm
    permission_required = 'structschool.change_structschool'


class StructCreateView(StructBaseView, CreateView):
    'createview'
    templatename = 'school/struct/structschool_form.html'
    form_class = StructSchoolForm
    permission_required = 'structschool.add_structschool'


class StructUpdateView(StructBaseView, UpdateView):
    'updadeview'
    templatename = 'school/struct/structschool_form.html'
    form_class = StructSchoolForm
    permission_required = 'structschool.change_structschool'


class StructDeleteView(StructBaseView, DeleteView):
    'deleteview'
    templatename = 'school/struct/structschool_confirm_delete.html'
    permission_required = 'structschool.delete_structschool'
