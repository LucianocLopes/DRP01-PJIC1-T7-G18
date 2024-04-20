from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse_lazy
from .models import CalendarEvent
from .forms import CalendarEventForm
from .util import events_to_json, calendar_options


# This is just an example for this demo. You may get this value
# from a separate file or anywhere you want

OPTIONS = """{  locale: 'pt-br',

                weekNumbers: true,
                
                views: {
                    timeGrid: {
                        dayMaxEventRows: 6
                    }
                },

                headerToolbar: {
                    left: '',
                    center: '',
                },

                businessHours: {
                
                    daysOfWeek: [ 1, 2, 3, 4, 5],
                
                    startTime: '07:00',
                    endTime: '12:00',
                    
                    startTime: '13:00',
                    endTime: '18:00', 
                },

                selectable: true,
                selectMirror: true,

                editable: true,
                eventLimit: 3,
                
            }"""


def index(request):
    event_url = 'all_events/'
    initial_grid = 'dayGridMonth'
    return render(request, 'schedule/scheduling.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
    )


def all_events(request):
    events = CalendarEvent.objects.all()
    return HttpResponse(events_to_json(events), content_type='application/json')


def day_events(request):
    event_url = 'all_events/'
    initial_grid = 'dayGridDay'
    return render(request, 'schedule/scheduling.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
    )


def week_events(request):
    event_url = 'all_events/'
    initial_grid = 'dayGridWeek'
    return render(request, 'schedule/scheduling.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
    )


def list_events(request):
    event_url = 'all_events/'
    initial_grid = 'listWeek'
    return render(request, 'schedule/scheduling.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
    )


class EventBaseView(PermissionRequiredMixin, View):
    model = CalendarEvent
    fields = '__all__'
    success_url = reverse_lazy('all')


class EventListView(EventBaseView, ListView):
    "list view"
    permission_required = 'calendarevent.view_calendarevent'


class EventDetailView(EventBaseView, DetailView):
    'detailview'
    permission_required = 'calendarevent.change_calendarevent'


class EventCreateView(EventBaseView, CreateView):
    'createview'
    form = CalendarEventForm
    permission_required = 'calendarevent.add_calendarevent'


class EventUpdateView(EventBaseView, UpdateView):
    'updadeview'
    permission_required = 'calendarevent.add_calendarevent'


class EventDeleteView(EventBaseView, DeleteView):
    'deleteview'
    permission_required = 'calendarevent.delete_calendarevent'
