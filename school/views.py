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

from .models import School, StructSchool

from .forms import SchoolForm, StructSchoolForm


class SchoolBaseView(PermissionRequiredMixin, View):
    model = School
    templatename = 'school/school_list.html'
    success_url = reverse_lazy('school_all')
    
    


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
<<<<<<< HEAD
>>>>>>> 70b58ba (add app school and config pages)
=======
    permission_required = 'school.delete_school'
<<<<<<< HEAD
>>>>>>> 4d331fd (corrections pages and acesses permissions)
=======


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
>>>>>>> 98c1c6d (corrects on apps)
