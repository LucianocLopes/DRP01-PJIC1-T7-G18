from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from school.models import School
from .models import Student

from .forms import StudentForm


class StudentBaseView(PermissionRequiredMixin, View):
    model = Student
    templatename = 'student/student_list.html'
    fields = '__all__'
    success_url = reverse_lazy('student_all')

    def get_context_data(self, **kwargs):
        context = super(StudentBaseView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context

class StudentListView(StudentBaseView, ListView):
    "list view"
    paginate_by = 25
    permission_required = 'student.view_student'


class StudentDetailView(StudentBaseView, DetailView):
    'detailview'
    form = StudentForm
    permission_required = 'student.change_student'


class StudentCreateView(StudentBaseView, CreateView):
    'createview'
    form = StudentForm
    permission_required = 'student.add_student'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StudentUpdateView(StudentBaseView, UpdateView):
    'updadeview'
    form = StudentForm
    permission_required = 'student.change_student'


class StudentDeleteView(StudentBaseView, DeleteView):
    'deleteview'
    permission_required = 'student.delete_student'
