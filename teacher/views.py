from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from school.models import School

from .models import Teacher

from .forms import TeacherForm


class TeacherBaseView(PermissionRequiredMixin, View):
    model = Teacher
    templatename = 'teacher/teacher_list.html'
    success_url = reverse_lazy('teacher_all')
    form_class = TeacherForm
    
    def get_context_data(self, **kwargs):
        context = super(TeacherBaseView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context


class TeacherListView(TeacherBaseView, ListView):
    "list view"
    paginate_by = 10
    permission_required = 'teacher.view_teacher'


class TeacherDetailView(TeacherBaseView, DetailView):
    'detailview'
    permission_required = 'teacher.change_teacher'


class TeacherCreateView(TeacherBaseView, CreateView):
    'createview'
    permission_required = 'teacher.add_teacher'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TeacherUpdateView(TeacherBaseView, UpdateView):
    'updadeview'
    permission_required = 'teacher.change_teacher'


class TeacherDeleteView(TeacherBaseView, DeleteView):
    'deleteview'
    permission_required = 'teacher.delete_teacher'
