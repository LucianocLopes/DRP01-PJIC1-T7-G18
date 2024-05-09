from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from school.models import School


class Graduation(models.Model):

    name = models.CharField(_("Nome da Graduação"), max_length=20)
    school = models.ForeignKey(
        School, 
        verbose_name=_("Escola"),
        on_delete=models.PROTECT,
    )
    teacher = models.ForeignKey(
        "Teacher", 
        verbose_name=_("Professor(a)"), 
        on_delete=models.PROTECT,
    )
    disciplines = models.ManyToManyField(
        "Discipline", 
        verbose_name=_("Disciplinas"),
    )

    class Meta:
        verbose_name = _("Graduação")
        verbose_name_plural = _("Gratuações")

    def __str__(self):
        return self.name.title()


class Discipline(models.Model):

    name = models.CharField(_("Disciplina"), max_length=15)
    disciplines = models.ManyToManyField(
        'Discipline', verbose_name=_("Disciplina"))

    class Meta:
        verbose_name = _("Disciplina")
        verbose_name_plural = _("Disciplinas")

    def __str__(self):
        return self.name.title()

