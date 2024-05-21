from django.views import View
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from school.models import School

from .forms import GroupForm
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from group.models import DayWeek_Choice, Group, GridGroup
from .models import GridGroup, Group
from .forms import GridGroupForm, GroupForm


class GridGroupDetailView(DetailView):
    model = GridGroup
    template_name = "group/gridgroup_detail.html"
    success_url = reverse_lazy('group_all')

class GridGroupListView(ListView):
    model = GridGroup
    template_name = "group/gridgroup_list.html"
    form_class = GridGroupForm
    success_url = reverse_lazy('group_all')


class GridGroupCreateView(CreateView):
    model = GridGroup
    template_name = "group/gridgroup_form.html"
    form_class = GridGroupForm
    success_url = reverse_lazy('group_all')




class GroupBaseView(PermissionRequiredMixin, View):
    model = Group
    success_url = reverse_lazy('group_all')

    def get_context_data(self, **kwargs):
        context = super(GroupBaseView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context

class GroupListView(GroupBaseView, ListView):
    "list view"
    paginate_by = 10
    permission_required = 'group.view_group'
    form_class = GroupForm


class GroupDetailView(GroupBaseView, DetailView):
    'detailview'
    permission_required = 'group.change_group'
    form_class = GroupForm


class GroupCreateView(GroupBaseView, CreateView):
    'createview'
    form_class = GroupForm
    permission_required = 'group.add_group'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroupUpdateView(GroupBaseView, UpdateView):
    'updadeview'
    permission_required = 'group.change_group'
    form_class = GroupForm
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroupDeleteView(GroupBaseView, DeleteView):
    'deleteview'
    permission_required = 'group.delete_group'


class GroupStudentsView(GroupBaseView, DetailView):
    'students_detail_view'
    template_name = 'group/group_students.html'
    permission_required = 'group.add_group'

    def get_context_data(self, **kwargs):
        context = super(GroupStudentsView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context