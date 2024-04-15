from pi1tg18.settings import base

# django-fullcalendar static file location defaults to FullCalendar default
# folder structure, expected to be under the STATIC_URL

FULLCALENDAR_DEFAULTS = {
    'javascript_url': '//cdn.jsdelivr.net/npm/fullcalendar@6.1.11/index.global.min.js',
}

# Updates location based on configuration defined by
# settings.py of the project

FULLCALENDAR = FULLCALENDAR_DEFAULTS.copy()
FULLCALENDAR.update(getattr(base, 'FULLCALENDAR', {}))


def javascript_url():
    return FULLCALENDAR['javascript_url']
