<<<<<<< HEAD
<<<<<<< HEAD
from .views import *

=======
from .views import index, all_events, add_event, list_events, day_events, week_events
>>>>>>> 16093fb (created app schedule, config and tests)
=======
from .views import index, all_events, list_events, day_events, week_events, EventCreateView, EventDeleteView, EventDetailView, EventUpdateView, EventListView
>>>>>>> ac9891b (corrections apps)
from django.urls import path


urlpatterns = [
    path("", index, name="scheduling"),
    path("all_events/", all_events, name="all_events"),
    path("list_events/", list_events, name="list_events"),
    path("day_events/", day_events, name="day_events"),
    path("week_events/", week_events, name="week_events"),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path("events/", EventListView.as_view(), name="event_all"),
=======
    path("events/", EventListView.as_view(), name="all"),
>>>>>>> ac9891b (corrections apps)
=======
    path("events/", EventListView.as_view(), name="event_all"),
>>>>>>> 98c1c6d (corrects on apps)
    path('events/<int:pk>/detail', EventDetailView.as_view(), name='event_detail'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
<<<<<<< HEAD
=======
    path("add_event/", add_event, name="add_event"),
>>>>>>> 16093fb (created app schedule, config and tests)
=======
>>>>>>> ac9891b (corrections apps)
]
