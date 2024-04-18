from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Teacher

from .forms import TeacherForm


class TeacherBaseView(View):
    model = Teacher
    templatename = 'teacher/teacher_list.html'
    fields = '__all__'
    success_url = reverse_lazy('teacher_all')


class TeacherListView(TeacherBaseView, ListView):
    "list view"


class TeacherDetailView(TeacherBaseView, DetailView):
    'detailview'
    form = TeacherForm


class TeacherCreateView(TeacherBaseView, CreateView):
    'createview'
    form = TeacherForm


class TeacherUpdateView(TeacherBaseView, UpdateView):
    'updadeview'
    form = TeacherForm


class TeacherDeleteView(TeacherBaseView, DeleteView):
    'deleteview'
