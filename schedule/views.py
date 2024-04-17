from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
<<<<<<< HEAD
=======
from django.http import HttpRequest, HttpResponse
>>>>>>> ac9891b (corrections apps)
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
<<<<<<< HEAD

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
                
=======
=======
from django.urls import reverse_lazy
>>>>>>> ac9891b (corrections apps)
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

>>>>>>> 16093fb (created app schedule, config and tests)
            }"""


def index(request):
<<<<<<< HEAD
    event_url = 'schedule/all_events/'
    default_view = "dayGridMonth"
    school = School.objects.all().annotate().first()
    
    return render(request, 'schedule/scheduling.html', {
        'school': school,
        'calendar_config_options': calendar_options(event_url, default_view, OPTIONS)}
=======
    event_url = 'all_events/'
    initial_grid = 'dayGridMonth'
    return render(request, 'schedule/scheduling.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
>>>>>>> 16093fb (created app schedule, config and tests)
    )


def all_events(request):
    events = CalendarEvent.objects.all()
<<<<<<< HEAD
    
=======
>>>>>>> 16093fb (created app schedule, config and tests)
    return HttpResponse(events_to_json(events), content_type='application/json')


def day_events(request):
<<<<<<< HEAD
    event_url = 'schedule/all_events/'
    default_view = "timeGrid"
    school = School.objects.all().annotate().first()
    
    return render(request, 'schedule/scheduling.html', {
        'school': school,
        'calendar_config_options': calendar_options(event_url, default_view, OPTIONS)}
=======
    event_url = 'all_events/'
    initial_grid = 'dayGridDay'
    return render(request, 'schedule/day_events.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
>>>>>>> 16093fb (created app schedule, config and tests)
    )


def week_events(request):
<<<<<<< HEAD
    event_url = 'schedule/all_events/'
    default_view = "timeGridWeek"
    school = School.objects.all().annotate().first()
    
    return render(request, 'schedule/scheduling.html', {
        'school': school,
        'calendar_config_options': calendar_options(event_url, default_view, OPTIONS)}
=======
    event_url = 'all_events/'
    initial_grid = 'dayGridWeek'
    return render(request, 'schedule/week_events.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
>>>>>>> 16093fb (created app schedule, config and tests)
    )


def list_events(request):
<<<<<<< HEAD
    event_url = 'schedule/all_events/'
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
=======
    event_url = 'all_events/'
    initial_grid = 'listWeek'
    return render(request, 'schedule/list_events.html', {
        'calendar_config_options': calendar_options(event_url, initial_grid, OPTIONS)}
    )


<<<<<<< HEAD
def add_event(request):
    start = request.GET.get('start', None)
    end = request.GET.get('end', None)
    title = request.GET.get('title', None)
    event = CalendarEvent(name=str(title), start=start, end=end)
    event.save
    data = {}
    return HttpResponse(events_to_json(data), content_tyoe="application/json")
>>>>>>> 16093fb (created app schedule, config and tests)
=======
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
>>>>>>> ac9891b (corrections apps)
