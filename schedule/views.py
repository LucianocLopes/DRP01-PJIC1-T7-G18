from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
                        dayMaxEventRows: 4 // adjust to 6 only for timeGridWeek/timeGridDay
                    }
                },

                headerToolbar: {
                    left: 'newButton',
                    center: 'title',
                },
                businessHours: {
                    // days of week. an array of zero-based day of week integers (0=Sunday)
                    daysOfWeek: [ 1, 2, 3, 4, 5], //

                    startTime: '08:00', // a start time (10am in this example)
                    endTime: '20:00', // an end time (6pm in this example)
                },

                selectable: true,
                selectMirror: true,

                editable: true,
                eventLimit: 6,
                
                customButtons: {
                        newButton: {
                        text: 'Novo',
                        click: function() {
                            alert('clicked the custom button!');
                        }
                    }
                },

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
    return render(request, 'schedule/day_events.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
    )


def week_events(request):
    event_url = 'all_events/'
    initial_grid = 'dayGridWeek'
    return render(request, 'schedule/week_events.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
    )


def list_events(request):
    event_url = 'all_events/'
    initial_grid = 'listWeek'
    return render(request, 'schedule/list_events.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
    )


class EventBaseView(View):
    model = CalendarEvent
    templatename = 'schedule/crud/list.html'
    fields = '__all__'
    success_url = reverse_lazy('all')


class EventListView(EventBaseView, ListView):
    "list view"


class EventDetailView(EventBaseView, DetailView):
    'detailview'


class EventCreateView(EventBaseView, CreateView):
    'createview'
    form = CalendarEventForm


class EventUpdateView(EventBaseView, UpdateView):
    'updadeview'


class EventDeleteView(EventBaseView, DeleteView):
    'deleteview'
