from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import School

from .forms import SchoolForm


class SchoolBaseView(View):
    model = School
    templatename = 'school/school_list.html'
    fields = '__all__'
    success_url = reverse_lazy('all')


class SchoolListView(SchoolBaseView, ListView):
    "list view"


class SchoolDetailView(SchoolBaseView, DetailView):
    'detailview'
    form = SchoolForm


class SchoolCreateView(SchoolBaseView, CreateView):
    'createview'
    form = SchoolForm


class SchoolUpdateView(SchoolBaseView, UpdateView):
    'updadeview'
    form = SchoolForm


class SchoolDeleteView(SchoolBaseView, DeleteView):
    'deleteview'
