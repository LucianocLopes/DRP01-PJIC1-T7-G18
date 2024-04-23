from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q


from core.models import TimeStamp
from student.models import Student
from discipline.models import Graduation
from school.models import School, StructSchool
from teacher.models import Teacher


class IdentificationGroupChoice(models.TextChoices):
    A = 'A',
    B = 'B',
    c = 'C',
    D = 'D',
    E = 'E',
    F = 'F',
    G = 'G',
    H = 'H',
    I = 'I',
    J = 'J',
    K = 'K',
    L = 'L',
    M = 'M',
    N = 'N',
    O = 'O',


class Group(TimeStamp):

    identification_group = models.CharField(_("Nome"),
                                            max_length=1,
                                            choices=IdentificationGroupChoice.choices,
                                            )

    school = models.ForeignKey(
        School,
        verbose_name=_("Escola"),
        on_delete=models.CASCADE,
    )

    graduation = models.ForeignKey(
        Graduation,
        verbose_name=_("Graduação"),
        on_delete=models.CASCADE,
    )

    localization = models.ForeignKey(
        StructSchool,
        verbose_name=_("Localização"),
        on_delete=models.CASCADE,
    )

    teacher_manager = models.ForeignKey(
        Teacher,
        verbose_name=_("Professor Responável"),
        on_delete=models.CASCADE,
    )

    students = models.ManyToManyField(
        Student,
        verbose_name=_("Estudantes"))

    class Meta:

        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'

    def name(self):

        return f'{self.graduation}-{self.name} '

    @property
    def get_information(self):
        result = Group.objects.values().annotate(
            matriculados=models.Count('students', filter=Q(id=self.id)),
        )
        return result

    @property
    def get_vagas(self):
        result = self.localization.vagas - self.get_matriculados
        return result

    @ property
    def get_matriculados(self):
        query = self.get_information
        for alunos in query:
            if alunos['id'] == self.id:
                return alunos['matriculados']

    def __str__(self):

        return f'{self.graduation} - {self.name}'

    def get_fields(self):

        return [(field.verbose_name, field.value_from_object(self))
                for field in self.__class__._meta.fields[1:]
                ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(Group, self).save_model(request, obj, form, change)
