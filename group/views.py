from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Group

from .forms import GroupForm


class GroupBaseView(PermissionRequiredMixin, View):
    model = Group
    templatename = 'group/group_list.html'
    fields = '__all__'
    success_url = reverse_lazy('group_all')


class GroupListView(GroupBaseView, ListView):
    "list view"
    permission_required = 'group.view_group'


class GroupDetailView(GroupBaseView, DetailView):
    'detailview'
    form = GroupForm
    permission_required = 'group.change_group'


class GroupCreateView(GroupBaseView, CreateView):
    'createview'
    form = GroupForm
    permission_required = 'group.add_group'

    def form_valid(self, form):
        name_id = form.instance.identification_group
        name_cl = form.instance.graduation.name
        print(name_id, name_cl)
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroupUpdateView(GroupBaseView, UpdateView):
    'updadeview'
    form = GroupForm
    permission_required = 'group.change_group'


class GroupDeleteView(GroupBaseView, DeleteView):
    'deleteview'
    permission_required = 'group.delete_group'
