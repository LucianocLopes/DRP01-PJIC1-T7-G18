from django.db import models
<<<<<<< HEAD
<<<<<<< HEAD
from django.utils.translation import gettext_lazy as _

=======
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import TimeStamp

>>>>>>> 16093fb (created app schedule, config and tests)
=======
from django.utils.translation import gettext_lazy as _

>>>>>>> 8b7b00c (corrections in apps views, forms and templates)

# Create your models here.

class CalendarEvent(models.Model):
<<<<<<< HEAD
<<<<<<< HEAD
    title = models.CharField(
        _('Compromisso'), blank=True, null=True, max_length=200)
    start = models.DateTimeField(_('Inicia em'), help_text='Data DD/MM/AAAA e Hora HH:MM')
    end = models.DateTimeField(
        _('Termina em'), null=True, blank=True, help_text='Data DD/MM/AAAA e Hora HH:MM')
    all_day = models.BooleanField(
        _('Dia Inteiro?'), default=False, blank=False, null=False)

    class Meta:
        verbose_name = _('Evento')
        verbose_name_plural = _('Eventos')
        ordering = ['start']

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                for field in self.__class__._meta.fields[1:]
                ]

    def __str__(self):
=======
    title = models.CharField(_('Title'), blank=True, max_length=200)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    all_day = models.BooleanField(_('All day'), default=False)
=======
    title = models.CharField(
        _('Titulo do Evento'), blank=True, null=True, max_length=200)
    start = models.DateTimeField(_('Inicia em'))
    end = models.DateTimeField(
        _('Termina em'), null=True, blank=True)
    all_day = models.BooleanField(
        _('Dia Inteiro?'), default=False, blank=False, null=False)
>>>>>>> 8b7b00c (corrections in apps views, forms and templates)

    class Meta:
        verbose_name = _('Evento')
        verbose_name_plural = _('Eventos')

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                for field in self.__class__._meta.fields[1:]
                ]

<<<<<<< HEAD
    def __str__(self) -> str:
>>>>>>> 16093fb (created app schedule, config and tests)
=======
    def __str__(self):
>>>>>>> 8b7b00c (corrections in apps views, forms and templates)
        return self.title
