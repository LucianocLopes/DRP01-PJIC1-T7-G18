from django.views.generic.base import TemplateView

from school.models import SchoolYear
from group.models import DayWeek_Choice, Group, GridGroup


class IndexView(TemplateView):
    template_name = "school/index.html"
    
    def get_context_data(self, **kwargs) -> dict:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['group'] = Group.objects.select_related().all().first()
        context['grid_group'] = GridGroup.objects.select_related().all()
        return context
    
