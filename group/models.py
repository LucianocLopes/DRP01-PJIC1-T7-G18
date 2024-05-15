from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta

from school.models import School, ClassRoom, TurnSchool, SchoolYear
from teacher.models import Teacher
from graduation.models import Graduation, Discipline


class GroupId_Choice(models.TextChoices):
    A = 'A', _('A')
    B = 'B', _('B')
    C = 'C', _('C')
    D = 'D', _('D')
    E = 'E', _('E')
    F = 'F', _('F')
    G = 'G', _('G')


class DayWeek_Choice(models.TextChoices):
    SUNDAY = 'sunday', _('Domingo')
    MONDAY = 'monday', _('Segunda-Feira')
    TUESDAY = 'tuesday', _("Terca-Feira")
    WEDNESDAY = 'wednesday', _('Quarta-Feira')
    THURSDAY = 'thursday', _('Quinta-Feira')
    FRIDAY = 'friday', _('Sexta-Feira')
    SATURDAY = 'saturday', _('Sábado')

class Discipline_Choice(models.TextChoices):
    MATH = 'math', _('Matemática')
    HISTORY = 'history', _('História')
    GEOGRAPHY = 'geography', _('Geografia')
    SCIENCE = 'science', _('Ciência')
    ART = 'art', _('Artes')
    ENGLISH = 'english', _('Inglês')
    SPANISH = 'spanish', _('Espanhol')
    FRENCH = 'french', _('Francês')
    DRAMATICS = 'dramatics', _('Dramartugia')
    PHYSCIALEDucATION = 'physicaleducation', _('Educação Física')
    WOODSHOP = 'woodshop', _('Marcenaria')
    HEALTH = 'health', _('Saúde')
    ECONOMICS = 'economics', _('Econômia')


class Group(models.Model):
    classroom = models.ForeignKey(
        ClassRoom, 
        verbose_name=_("Sala de Aula"), 
        on_delete=models.CASCADE,
    )
    graduation = models.ForeignKey(
        Graduation, 
        verbose_name=_("Graduação"), 
        on_delete=models.CASCADE,
    )
    group_id = models.CharField(_("Identificador"), max_length=1, choices=GroupId_Choice.choices, default='A')
    school_year = models.ForeignKey(
        SchoolYear, 
        verbose_name=_("Ano Letivo"), 
        on_delete=models.CASCADE
    )
    turn = models.ForeignKey(
        TurnSchool, 
        verbose_name=_("Turno"), 
        on_delete=models.CASCADE
    )
    interval_start = models.TimeField(_("Inicio do intervalo"), null=True, blank=True)
    interval_duration = models.PositiveIntegerField(_("Duração do Intervalo"), null=True, blank=True)

    class Meta:
        verbose_name = _("Classe")
        verbose_name_plural = _("Classes")

    def __str__(self):
        return f'{self.graduation} {self.group_id}'
    
    @property
    def get_start(self):
        start = self.interval_start.strftime('%H%M')
        return start

    @property
    def get_interval_end(self):
        data = datetime.now()
        start = datetime(year=data.year, month=data.month, day=data.day, hour=self.interval_start.hour, minute=self.interval_start.minute)
        end = self.interval_duration
        end_time = start + timedelta(minutes=end)
        print(end_time)
        return end_time.strftime("%H%M")

    @property
    def get_duration_interval(self):
        return f'{self.interval_duration / 60 } h'

class GridGroup(models.Model):

    group = models.ForeignKey(
        Group, 
        verbose_name=_("Classe"), 
        on_delete=models.CASCADE
    )
    day_week = models.CharField(_("Dia da Semana"), max_length=15, choices=DayWeek_Choice.choices)
    time_start = models.TimeField(_("Horario inicial"))
    duration_lesson = models.PositiveIntegerField(_("Duração (minutos)"), default=60, help_text='Informe um intervalo em minutos')
    dicipline = models.CharField(_("Diciplina"), max_length=20, choices=Discipline_Choice.choices, null=True, blank=True)
    teacher = models.ForeignKey(
        Teacher, 
        verbose_name=_("Professor"), 
        on_delete=models.CASCADE
    )
    description = models.CharField(_("Descrição"), max_length=254)
    @property
    def get_start(self):
        start = self.time_start.strftime('%H%M')
        return start
    
    @property
    def get_end_lesson(self):
        data = datetime.now()
        start = datetime(year=data.year, month=data.month, day=data.day, hour=self.time_start.hour, minute=self.time_start.minute)
        end = self.duration_lesson
        end_time = start + timedelta(minutes=end)
        
        return end_time.strftime("%H%M")
    
    @property
    def get_duration_time(self):
        return f'{self.duration_lesson / 60 } h'
    
    class Meta:
        verbose_name = _("GripGroup")
        verbose_name_plural = _("GripGroups")

    def __str__(self):
        return f''
