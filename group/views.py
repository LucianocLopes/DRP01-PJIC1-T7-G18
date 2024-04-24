from django.views import View
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
from django.views.generic import TemplateView
>>>>>>> 64cbb11 (configurations and edits apps)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
>>>>>>> 93b9589 (add and config new app group)
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

<<<<<<< HEAD
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


=======
from .models import Group

from .forms import GroupForm
>>>>>>> 93b9589 (add and config new app group)


class GroupBaseView(PermissionRequiredMixin, View):
    model = Group
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    templatename = 'group/group_list.html'
    fields = '__all__'
=======
>>>>>>> 64cbb11 (configurations and edits apps)
    success_url = reverse_lazy('group_all')


class GroupListView(GroupBaseView, ListView):
    "list view"
    permission_required = 'group.view_group'
<<<<<<< HEAD
>>>>>>> 93b9589 (add and config new app group)
=======
    form_class = GroupForm
>>>>>>> 64cbb11 (configurations and edits apps)


class GroupDetailView(GroupBaseView, DetailView):
    'detailview'
<<<<<<< HEAD
<<<<<<< HEAD
    permission_required = 'group.change_group'
    form_class = GroupForm
=======
    form = GroupForm
    permission_required = 'group.change_group'
>>>>>>> 93b9589 (add and config new app group)
=======
    permission_required = 'group.change_group'
    form_class = GroupForm
>>>>>>> 64cbb11 (configurations and edits apps)


class GroupCreateView(GroupBaseView, CreateView):
    'createview'
<<<<<<< HEAD
<<<<<<< HEAD
    form_class = GroupForm
    permission_required = 'group.add_group'

    def form_valid(self, form):
=======
    form = GroupForm
    permission_required = 'group.add_group'

    def form_valid(self, form):
        name_id = form.instance.identification_group
        name_cl = form.instance.graduation.name
        print(name_id, name_cl)
>>>>>>> 93b9589 (add and config new app group)
=======
    form_class = GroupForm
    permission_required = 'group.add_group'

    def form_valid(self, form):
        for student in form.students.all():
            if not student.registered:
                student.matricular()

>>>>>>> 64cbb11 (configurations and edits apps)
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroupUpdateView(GroupBaseView, UpdateView):
    'updadeview'
<<<<<<< HEAD
<<<<<<< HEAD
    permission_required = 'group.change_group'
    form_class = GroupForm
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
=======
    form = GroupForm
    permission_required = 'group.change_group'
>>>>>>> 93b9589 (add and config new app group)
=======
    permission_required = 'group.change_group'
    form_class = GroupForm
>>>>>>> 64cbb11 (configurations and edits apps)


class GroupDeleteView(GroupBaseView, DeleteView):
    'deleteview'
    permission_required = 'group.delete_group'
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 64cbb11 (configurations and edits apps)


class GroupStudentsView(GroupBaseView, DetailView):
    'students_detail_view'
    template_name = 'group/group_students.html'
    permission_required = 'group.add_group'
<<<<<<< HEAD

    def get_context_data(self, **kwargs):
        context = super(GroupStudentsView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context
=======
>>>>>>> 93b9589 (add and config new app group)
=======
>>>>>>> 64cbb11 (configurations and edits apps)
