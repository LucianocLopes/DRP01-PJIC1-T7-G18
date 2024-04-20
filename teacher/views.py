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
    permission_required = 'teacher.delete_teacher'
