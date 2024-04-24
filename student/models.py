from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStamp


class Student(TimeStamp):

    registered = models.BooleanField(
        _("Matriculado"), default=False, null=True, blank=True)

    first_name = models.CharField(_("Primeiro Nome"), max_length=50)
    last_name = models.CharField(_("Sobrenome"), max_length=70)

    mother_name = models.CharField(_("Noma da Mãe"), max_length=100)
    father_name = models.CharField(
        _("Nome do Pai"), max_length=100, blank=True, null=True)

    email = models.EmailField(_("E-mail"), max_length=254)

    phone_ddd = models.CharField(_("DDD"), max_length=4)
    phone_number = models.CharField(_("Telefone"), max_length=9)

    address_zipcode = models.CharField(_("CEP"), max_length=9)
    address = models.CharField(_("Endereço"), max_length=150)
    address_number = models.CharField(_("Número"), max_length=5)
    address_complement = models.CharField(_("Complemento"), max_length=20)
    address_district = models.CharField(_("Bairro"), max_length=50)
    address_city = models.CharField(_("Cidade"), max_length=70)
    address_state = models.CharField(_("UF"), max_length=2)

    class Meta:

        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def full_name(self):

        return f'{self.first_name.upper()} {self.last_name.upper()}'

    def __str__(self):

        return self.first_name

    def get_fields(self):

        return [(field.verbose_name, field.value_from_object(self))
                for field in self.__class__._meta.fields[1:]
                ]

    def save_model(self, request, obj, form, change):
        if not change:
            self.registered = False
            obj.user = request.user
            obj.save()
        super(Student, self).save_model(request, obj, form, change)

    def matricular(self):
        if not self.registered:
            self.registered = True

    def cancelar_matricula(self):
        if self.registered:
            self.registered = False


class RegisteredManager(models.Manager):
    def get_queryset(self):
        return super(RegisteredManager, self).get_queryset().filter(
            registered=True)


class NoRegisteredManager(models.Manager):
    def get_queryset(self):
        return super(NoRegisteredManager, self).get_queryset().filter(
            registered=False)


class StudentResgistred(Student):
    objects = RegisteredManager()

    class Meta:
        verbose_name = 'Aluno Matriculado'
        verbose_name_plural = 'Alunos Matriculados'
        proxy = True

    def save(self, *args, **kwargs):
        kwargs['registered'] = True
        return super().save(*args, **kwargs)


class StudentNoResgistred(Student):
    objects = NoRegisteredManager()

    class Meta:
        verbose_name = 'Aluno Não Matriculado'
        verbose_name_plural = 'Alunos Não Matriculados'
        proxy = True

    def save(self, *args, **kwargs):
        kwargs['registered'] = False
        return super().save(*args, **kwargs)
