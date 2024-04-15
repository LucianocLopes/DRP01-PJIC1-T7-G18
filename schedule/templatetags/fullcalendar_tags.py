from django import template
from django.utils.safestring import mark_safe
from schedule.fullcalendar import javascript_url

register = template.Library()


@register.inclusion_tag("schedule/calendar.html")
def calendar():
    return {}


@register.inclusion_tag("schedule/calendar_init.html")
def calendar_init(calendar_config_options):
    return {'calendar_config_options': mark_safe(calendar_config_options)}


@register.simple_tag
def fullcalendar_javascript_url():
    return javascript_url()


@register.simple_tag
def fullcalendar_javascript():
    url = fullcalendar_javascript_url()
    return mark_safe("<script src='%s'></script>" % url)
