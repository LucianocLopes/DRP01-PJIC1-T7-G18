from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CalendarEvent(models.Model):
    title = models.CharField(
        _('Titulo do Evento'), blank=True, null=True, max_length=200)
    start = models.DateTimeField(_('Inicia em'))
    end = models.DateTimeField(
        _('Termina em'), null=True, blank=True)
    all_day = models.BooleanField(
        _('Dia Inteiro?'), default=False, blank=False, null=False)

    class Meta:
        verbose_name = _('Evento')
        verbose_name_plural = _('Eventos')

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                for field in self.__class__._meta.fields[1:]
                ]

    def __str__(self):
        return self.title
