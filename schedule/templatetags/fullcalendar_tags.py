from django import template
from django.utils.safestring import mark_safe
<<<<<<< HEAD
<<<<<<< HEAD
from schedule.fullcalendar import *

=======
from schedule.fullcalendar import javascript_url
>>>>>>> 16093fb (created app schedule, config and tests)
=======
from schedule.fullcalendar import javascript_url, core_url, core_ptbr_url, daygrid_url, interaction_url, list_url, luxon_url, moment_url, moment_timezone_url, rrule_url, timegrid_url
>>>>>>> 98c1c6d (corrects on apps)

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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 98c1c6d (corrects on apps)
    return mark_safe("<script src='/static/%s'></script>" % url)


@register.simple_tag
def fullcalendar_core_url():
    return core_url()


@register.simple_tag
def fullcalendar_core():
    url = fullcalendar_core_url()
    return mark_safe("<script src='/static/%s'></script>" % url)


@register.simple_tag
def fullcalendar_core_ptbr_url():
    return core_ptbr_url()


@register.simple_tag
def fullcalendar_core_ptbr():
    url = fullcalendar_core_ptbr_url()
    return mark_safe("<script src='/static/%s'></script>" % url)


@register.simple_tag
def fullcalendar_daygrid_url():
    return daygrid_url()


@register.simple_tag
def fullcalendar_daygrid():
    url = fullcalendar_daygrid_url()
    return mark_safe("<script src='/static/%s'></script>" % url)


@register.simple_tag
def fullcalendar_interaction_url():
    return interaction_url()


@register.simple_tag
def fullcalendar_interaction():
    url = fullcalendar_interaction_url()
    return mark_safe("<script src='/static/%s'></script>" % url)


@register.simple_tag
def fullcalendar_list_url():
    return list_url()


@register.simple_tag
def fullcalendar_list():
    url = fullcalendar_list_url()
    return mark_safe("<script src='/static/%s'></script>" % url)


@register.simple_tag
def fullcalendar_luxon_url():
    return luxon_url()


@register.simple_tag
def fullcalendar_luxon():
    url = fullcalendar_luxon_url()
    return mark_safe("<script src='/static/%s'></script>" % url)


@register.simple_tag
def fullcalendar_moment_url():
    return moment_url()


@register.simple_tag
def fullcalendar_moment():
    url = fullcalendar_moment_url()
    return mark_safe("<script src='/static/%s'></script>" % url)


@register.simple_tag
def fullcalendar_moment_timezone_url():
    return moment_timezone_url()


@register.simple_tag
def fullcalendar_moment_timezone():
    url = fullcalendar_moment_timezone_url()
    return mark_safe("<script src='/static/%s'></script>" % url)


@register.simple_tag
def fullcalendar_rrule_url():
    return rrule_url()


@register.simple_tag
def fullcalendar_rrule():
    url = fullcalendar_rrule_url()
    return mark_safe("<script src='/static/%s'></script>" % url)


@register.simple_tag
def fullcalendar_timegrid_url():
    return timegrid_url()


@register.simple_tag
def fullcalendar_timegrid():
    url = fullcalendar_timegrid_url()
    return mark_safe("<script src='/static/%s'></script>" % url)
<<<<<<< HEAD
=======
    return mark_safe("<script src='%s'></script>" % url)
>>>>>>> 16093fb (created app schedule, config and tests)
=======
>>>>>>> 98c1c6d (corrects on apps)
