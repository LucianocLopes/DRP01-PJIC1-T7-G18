from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse_lazy
from .models import CalendarEvent
from .forms import CalendarEventForm
from .util import events_to_json, calendar_options

from school.models import School



OPTIONS = """{
                locale: 'pt-br',

                header: {
                    left: 'title',
                    center: '',
                    right: 'prev,next' 
                },
                
                businessHours: {
                    // days of week. an array of zero-based day of week integers (0=Sunday)
                    daysOfWeek: [ 1, 2, 3, 4, 5 ],

                    startTime: '06:30',
                    endTime: '18:00',
                },

                navLinks: true,

                editable: true,
                
                selectable: true,
                
                eventLimit: true,
                
                eventTimeFormat: { hour: 'numeric', minute: '2-digit', timeZoneName: 'short' },

                dateClick: function (arg) {
                    console.log('dateClick', calendar.formatIso(arg.date));
                },

                select: function (arg) {
                    console.log('select', calendar.formatIso(arg.start), calendar.formatIso(arg.end));
                },
                
            }"""


def index(request):
    event_url = 'all_events/'
    default_view = "dayGridMonth"
    school = School.objects.all().annotate().first()
    
    return render(request, 'schedule/scheduling.html', {
        'school': school,
        'calendar_config_options': calendar_options(event_url, default_view, OPTIONS)}
    )


def all_events(request):
    events = CalendarEvent.objects.all()
    
    return HttpResponse(events_to_json(events), content_type='application/json')


def day_events(request):
    event_url = 'all_events/'
    default_view = "timeGrid"
    school = School.objects.all().annotate().first()
    
    return render(request, 'schedule/scheduling.html', {
        'school': school,
        'calendar_config_options': calendar_options(event_url, default_view, OPTIONS)}
    )


def week_events(request):
    event_url = 'all_events/'
    default_view = "timeGridWeek"
    school = School.objects.all().annotate().first()
    
    return render(request, 'schedule/scheduling.html', {
        'school': school,
        'calendar_config_options': calendar_options(event_url, default_view, OPTIONS)}
    )


def list_events(request):
    event_url = 'all_events/'
    default_view = "timeGridMonth"
    school = School.objects.all().annotate().first()
    
    return render(request, 'schedule/scheduling.html', {
        'school': school,
        'calendar_config_options': calendar_options(event_url,  default_view, OPTIONS)}
    )


class EventBaseView(PermissionRequiredMixin, View):
    model = CalendarEvent
    success_url = reverse_lazy('event_all')

    def get_context_data(self, **kwargs):
        context = super(EventBaseView, self).get_context_data(**kwargs)
        context['school'] = School.objects.all().annotate().first()
        return context

class EventListView(EventBaseView, ListView):
    "list view"
    paginate_by = 10
    permission_required = 'calendarevent.view_calendarevent'
    form_class = CalendarEventForm


class EventDetailView(EventBaseView, DetailView):
    'detailview'
    permission_required = 'calendarevent.change_calendarevent'
    form_class = CalendarEventForm


class EventCreateView(EventBaseView, CreateView):
    'createview'
    permission_required = 'calendarevent.add_calendarevent'
    form_class = CalendarEventForm


class EventUpdateView(EventBaseView, UpdateView):
    'updadeview'
    permission_required = 'calendarevent.add_calendarevent'
    form_class = CalendarEventForm


class EventDeleteView(EventBaseView, DeleteView):
    'deleteview'
    permission_required = 'calendarevent.delete_calendarevent'
