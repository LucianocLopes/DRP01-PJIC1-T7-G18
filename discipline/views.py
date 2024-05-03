from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Discipline, Graduation

from .forms import DisciplineForm, GraduationForm


class DisciplineBaseView(PermissionRequiredMixin, View):
    model = Discipline
    templatename = 'discipline/discipline_list.html'
    success_url = reverse_lazy('discipline_all')
    form_class = DisciplineForm


class DisciplineListView(DisciplineBaseView, ListView):
    "list view"
    permission_required = 'discipline.view_discipline'


class DisciplineDetailView(DisciplineBaseView, DetailView):
    'detailview'
    permission_required = 'discipline.change_discipline'


class DisciplineCreateView(DisciplineBaseView, CreateView):
    'createview'
    permission_required = 'discipline.add_discipline'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DisciplineUpdateView(DisciplineBaseView, UpdateView):
    'updadeview'
    permission_required = 'discipline.change_discipline'


class DisciplineDeleteView(DisciplineBaseView, DeleteView):
    'deleteview'
    permission_required = 'discipline.delete_discipline'


class GraduationBaseView(PermissionRequiredMixin, View):
    model = Graduation
    templatename = 'graduation/graduation_list.html'
    success_url = reverse_lazy('graduation_all')
    form_class = GraduationForm


class GraduationListView(GraduationBaseView, ListView):
    "list view"
    paginate_by = 10
    permission_required = 'graduation.view_graduation'


class GraduationDetailView(GraduationBaseView, DetailView):
    'detailview'
    permission_required = 'graduation.change_graduation'


class GraduationCreateView(GraduationBaseView, CreateView):
    'createview'
    permission_required = 'graduation.add_graduation'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GraduationUpdateView(GraduationBaseView, UpdateView):
    'updadeview'
    permission_required = 'graduation.change_graduation'


class GraduationDeleteView(GraduationBaseView, DeleteView):
    'deleteview'
    permission_required = 'graduation.delete_graduation'
