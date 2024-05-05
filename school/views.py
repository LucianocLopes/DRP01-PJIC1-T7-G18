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
    
    def get_context_data(self, **kwargs):
        context = super(SchoolBaseView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context


class SchoolListView(SchoolBaseView, ListView):
    "list view"
    paginate_by = 10
    permission_required = 'school.view_school'


class SchoolDetailView(SchoolBaseView, DetailView):
    'detailview'
    form_class = SchoolForm
    permission_required = 'school.change_school'


class SchoolCreateView(SchoolBaseView, CreateView):
    'createview'
    form_class = SchoolForm
    permission_required = 'school.add_school'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
    
    def get_context_data(self, **kwargs):
        context = super(StructBaseView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context


class StructListView(StructBaseView, ListView):
    "list view"
    paginate_by = 10
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
