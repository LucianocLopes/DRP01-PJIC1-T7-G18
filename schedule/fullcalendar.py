<<<<<<< HEAD
from pi1t7g18.settings import base

FULLCALENDAR_DEFAULTS = {
    'javascript_url': 'vendor/fullcalendar/packages/interaction/main.min.js',
    'core_ptbr_url': 'vendor/fullcalendar/packages/core/locales/pt-br.js',
    'core_url': 'vendor/fullcalendar/packages/core/main.js',
    'daygrid_url': 'vendor/fullcalendar/packages/daygrid/main.js',
    'interaction_url': 'vendor/fullcalendar/packages/interaction/main.js',
    'list_url': 'vendor/fullcalendar/packages/list/main.js',
    'luxon_url': 'vendor/fullcalendar/packages/luxon/main.js',
    'moment_url': 'vendor/fullcalendar/packages/moment/main.js',
    'moment_timezone_url': 'vendor/fullcalendar/packages/moment-timezone/main.js',
    'rrule_url': 'vendor/fullcalendar/packages/rrule/main.js',
    'timegrid_url': 'vendor/fullcalendar/packages/timegrid/main.js',
=======
from pi1tg18.settings import base

FULLCALENDAR_DEFAULTS = {
<<<<<<< HEAD
    'javascript_url': '//cdn.jsdelivr.net/npm/fullcalendar@6.1.11/index.global.min.js',
>>>>>>> 16093fb (created app schedule, config and tests)
=======
    'javascript_url': 'vendor/fullcalendar/packages/interaction/main.min.js',
    'core_ptbr_url': 'vendor/fullcalendar/packages/core/locales/pt-br.js',
    'core_url': 'vendor/fullcalendar/packages/core/main.js',
    'daygrid_url': 'vendor/fullcalendar/packages/daygrid/main.js',
    'interaction_url': 'vendor/fullcalendar/packages/interaction/main.js',
    'list_url': 'vendor/fullcalendar/packages/list/main.js',
    'luxon_url': 'vendor/fullcalendar/packages/luxon/main.js',
    'moment_url': 'vendor/fullcalendar/packages/moment/main.js',
    'moment_timezone_url': 'vendor/fullcalendar/packages/moment-timezone/main.js',
    'rrule_url': 'vendor/fullcalendar/packages/rrule/main.js',
    'timegrid_url': 'vendor/fullcalendar/packages/timegrid/main.js',
>>>>>>> 98c1c6d (corrects on apps)
}

# Updates location based on configuration defined by
# settings.py of the project

FULLCALENDAR = FULLCALENDAR_DEFAULTS.copy()
FULLCALENDAR.update(getattr(base, 'FULLCALENDAR', {}))


def javascript_url():
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 98c1c6d (corrects on apps)

    return FULLCALENDAR['javascript_url']


def core_url():

    return FULLCALENDAR['core_url']


def core_ptbr_url():

    return FULLCALENDAR['core_ptbr_url']


def daygrid_url():

    return FULLCALENDAR['daygrid_url']


def interaction_url():

    return FULLCALENDAR['interaction_url']


def list_url():

    return FULLCALENDAR['list_url']


def luxon_url():

    return FULLCALENDAR['luxon_url']


def moment_url():

    return FULLCALENDAR['moment_url']


def moment_timezone_url():

    return FULLCALENDAR['moment_timezone_url']


def rrule_url():

    return FULLCALENDAR['rrule_url']


def timegrid_url():

    return FULLCALENDAR['timegrid_url']
<<<<<<< HEAD
=======
    return FULLCALENDAR['javascript_url']
>>>>>>> 16093fb (created app schedule, config and tests)
=======
>>>>>>> 98c1c6d (corrects on apps)
