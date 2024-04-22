from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStamp


class StructTypeChoice(models.TextChoices):
    SALADEAULA = 'SLAU', _('Sala de Aula')
    QUADRAPOLIESPORTIVA = 'QPE', _('Quadra Poliesportiva')
    ESPACORECREACAO = 'ESPR', _('Espaço de Recreação')
    SALAINFORMATIVA = 'SLIN', _('Sala de Informatica/Computação')
    LABORATORIO = 'LAB', _('Laboratório')
    PROFESSORES = 'PROF', _('Sala dos Professores')


class School(TimeStamp):

    name = models.CharField(_("Nome da Escola"), max_length=150)
    cnpj_number = models.CharField(_("CNPJ da Escola"), max_length=18)
    school_number = models.CharField(
        _("Numero Cadastro Secretaria"), max_length=20)

    address_zipcode = models.CharField(_("CEP"), max_length=9)
    address = models.CharField(_("Endereço"), max_length=150)
    address_number = models.CharField(_("Número"), max_length=5)
    address_complement = models.CharField(_("Complemento"), max_length=20)
    address_district = models.CharField(_("Bairro"), max_length=50)
    address_city = models.CharField(_("Cidade"), max_length=70)
    address_state = models.CharField(_("UF"), max_length=2)

    email = models.EmailField(_("E-mail"), max_length=254)
    phone_ddd = models.CharField(_("DDD"), max_length=4)
    phone_number = models.CharField(_("Phone"), max_length=9)

    class Meta:
        """Meta definition for School."""

        verbose_name = 'Escola'
        verbose_name_plural = 'Escola'

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                for field in self.__class__._meta.fields[1:]
                ]

    def __str__(self):
        """Unicode representation of School."""
        return self.name.upper()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(School, self).save_model(request, obj, form, change)


class StructSchool(models.Model):

    school = models.ForeignKey(
        School, verbose_name=_("Escola"), on_delete=models.CASCADE)

    name = models.CharField(_("Estrutura"), max_length=50)
    struct_type = models.CharField(
        _("Tipo de estrutura"), max_length=4, choices=StructTypeChoice.choices)
    height = models.IntegerField(_("Altura (m)"), blank=True, null=True)
    width = models.IntegerField(_("Largura (m)"), blank=True, null=True)
    length = models.IntegerField(_("Comprimento (m)"), blank=True, null=True)
    area = models.IntegerField(_("Area (m2)"))
    perimeter = models.IntegerField(_("Perímetro (m2)"))
    vagas = models.IntegerField(_("Quantidade de vagas"))

    class Meta:
        """Meta definition for StructSchool."""

        verbose_name = 'StructSchool'
        verbose_name_plural = 'StructSchools'

    def __str__(self):
        """Unicode representation of StructSchool."""
        return f'{self.struct_type} {self.name}'
