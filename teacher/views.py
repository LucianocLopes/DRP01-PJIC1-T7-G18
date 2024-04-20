<<<<<<< HEAD
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from group.models import DayWeek_Choice, Group, GridGroup
from .models import Teacher
from .forms import TeacherForm

from school.models import School

class TeacherGroupView(DetailView):
    model = Teacher
    template_name = "teacher/teacher_group.html"
    
    def get_context_data(self, **kwargs) -> dict:
        context = super(TeacherGroupView, self).get_context_data(**kwargs)
        context['school'] = School.objects.select_related().first()
        context['group'] = Group.objects.select_related().all().first()
        context['grid_group'] = GridGroup.objects.select_related().all()
        
        return context


class TeacherListView(ListView):
    model = Teacher
    template_name = "teacher/teacher_list.html"
    form_class = TeacherForm
    
    def get_context_data(self, **kwargs) -> dict:
        context = super(TeacherListView, self).get_context_data(**kwargs)
        context['school'] = School.objects.select_related().first()
        
        return context

class TeacherCreateView(CreateView):
    model = Teacher
    template_name = "teacher/teacher_form.html"
    form_class = TeacherForm
=======
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Teacher

from .forms import TeacherForm


class TeacherBaseView(PermissionRequiredMixin, View):
    model = Teacher
    templatename = 'teacher/teacher_list.html'
    fields = '__all__'
    success_url = reverse_lazy('teacher_all')


class TeacherListView(TeacherBaseView, ListView):
    "list view"
    permission_required = 'teacher.view_teacher'


class TeacherDetailView(TeacherBaseView, DetailView):
    'detailview'
    form = TeacherForm
    permission_required = 'teacher.change_teacher'


class TeacherCreateView(TeacherBaseView, CreateView):
    'createview'
    form = TeacherForm
    permission_required = 'teacher.add_teacher'


class TeacherUpdateView(TeacherBaseView, UpdateView):
    'updadeview'
    form = TeacherForm
    permission_required = 'teacher.change_teacher'


class TeacherDeleteView(TeacherBaseView, DeleteView):
    'deleteview'
<<<<<<< HEAD
>>>>>>> ee2e9db (add, configurate and edit app teacher)
=======
    permission_required = 'teacher.delete_teacher'
>>>>>>> 4d331fd (corrections pages and acesses permissions)
