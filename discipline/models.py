from django.db import models
import math
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import TimeStamp


class Discipline(TimeStamp):
    name = models.CharField(_("Nome da Disciplina"), max_length=50)
    duration = models.IntegerField(_("Duração (hrs/semana)"))

    class Meta:
        """Meta definition for Discipline."""

        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                for field in self.__class__._meta.fields[1:]
                ]

    def __str__(self):
        """Unicode representation of Discipline."""
        return self.name.title()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(Discipline, self).save_model(request, obj, form, change)


class Graduation(TimeStamp):

    name = models.CharField(_("Nome da Graduação"), max_length=50)
    disc = models.ManyToManyField(
        Discipline,
        verbose_name=_("Disciplinas"),
    )

    class Meta:
        """Meta definition for Graduation."""

        verbose_name = 'Graduação'
        verbose_name_plural = 'Graduações'

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                for field in self.__class__._meta.fields[1:]
                ]

    @property
    def duration_hours(self):

        result = Graduation.objects.filter(disc__graduation=self.id).annotate(
            All_hours=models.Sum('disc__duration'))
        if result:
            for num in result:
                hours = num.All_hours

            return hours

    def __str__(self):
        return self.name.title()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(Graduation, self).save_model(request, obj, form, change)
