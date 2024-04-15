from .views import index, all_events, add_event, list_events, day_events, week_events
from django.urls import path


urlpatterns = [
    path("", index, name="scheduling"),
    path("all_events/", all_events, name="all_events"),
    path("list_events/", list_events, name="list_events"),
    path("day_events/", day_events, name="day_events"),
    path("week_events/", week_events, name="week_events"),
    path("add_event/", add_event, name="add_event"),
]
