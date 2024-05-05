from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from school.models import School

from .models import Group

from .forms import GroupForm


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
        for student in form.students.all():
            if not student.registered:
                student.matricular()

        form.instance.user = self.request.user
        return super().form_valid(form)


class GroupUpdateView(GroupBaseView, UpdateView):
    'updadeview'
    permission_required = 'group.change_group'
    form_class = GroupForm


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