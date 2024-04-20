<<<<<<< HEAD
from django.views.generic.base import TemplateView

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from school.models import School, PhoneSchool, AddressSchool
from group.models import Group, GridGroup

from .forms import SchoolForm

class IndexView(TemplateView):
    template_name = "school/index.html"
    
    def get_context_data(self, **kwargs) -> dict:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['school'] = School.objects.select_related().first()
        context['group'] = Group.objects.select_related().all().first()
        context['grid_group'] = GridGroup.objects.select_related().all()
        return context
    

class SchoolDetailView(DetailView):
    # model = School
    form_class = SchoolForm
    template_name = 'school/crud/school_detail.html'
    queryset = School.objects.select_related()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["phones"] = PhoneSchool.objects.select_related().all()
        context["addresses"] = AddressSchool.objects.select_related().all()

        return context
    


class SchoolListView(ListView):
    template_name = "school/crud/school_list.html"
    form_class = SchoolForm
    queryset = School.objects.select_related().all()

    def get_context_data(self, **kwargs):
        context = super(SchoolListView, self).get_context_data(**kwargs)
        context['school'] = School.objects.select_related().first()
        context["phones"] = PhoneSchool.objects.select_related().all()
        context["addresses"] = AddressSchool.objects.select_related().all()

        return context


class SchoolUpdateView(UpdateView):
    template_name = "school/crud/school_form.html"
    form_class = SchoolForm
    queryset = School.objects.select_related().all()
    success_url = reverse_lazy('school_all')
    


class PhoneSchoolDetailView(DetailView):
    model = PhoneSchool
    template_name = ""
    


class PhoneSchoolListView(ListView):
    template_name = "school/crud/phone/list.html"
    queryset = PhoneSchool.objects.select_related().all()
    success_url = reverse_lazy('school_all')


class AddressSchoolDetailView(DetailView):
    model = AddressSchool
    template_name = "TEMPLATE_NAME"


class AddressSchoolListView(ListView):
    template_name = "school/crud/address/list.html"
    queryset = AddressSchool.objects.select_related().all()
    success_url = reverse_lazy('school_all')

=======
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
<<<<<<< HEAD
>>>>>>> 70b58ba (add app school and config pages)
=======
    permission_required = 'school.delete_school'
>>>>>>> 4d331fd (corrections pages and acesses permissions)
