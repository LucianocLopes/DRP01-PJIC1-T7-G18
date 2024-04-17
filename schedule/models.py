from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import TimeStamp


# Create your models here.

class CalendarEvent(models.Model):
    title = models.CharField(_('Title'), blank=True, max_length=200)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    all_day = models.BooleanField(_('All day'), default=False)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __unicode__(self):
        return self.title

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                for field in self.__class__._meta.fields[1:]
                ]

    def __str__(self) -> str:
        return self.title
