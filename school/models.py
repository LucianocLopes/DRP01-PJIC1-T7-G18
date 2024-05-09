from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from core.models import Address, PhoneBase


class School(models.Model):

    name = models.CharField(_("Nome da Escola"), max_length=100)
    fantasy_name = models.CharField(_("Apelido"), max_length=30)
    email = models.EmailField(_("E-mail"), max_length=254)

    class Meta:
        verbose_name = _("Escola")
        verbose_name_plural = _("Escolas")

    def __str__(self):
        return self.name.title()

    def get_fantasy(self):
        return self.fantasy_name.title()


class AddressSchool(models.Model):

    school = models.OneToOneField(
        School,
        verbose_name=_("Escola"),
        on_delete=models.CASCADE,
    )
    address = models.ForeignKey(
        Address,
        verbose_name=_("Endereço"),
        on_delete=models.PROTECT,
    )
    number = models.IntegerField(_("Número"))
    complement = models.CharField(_("Complemento"), max_length=20, blank=True, null=True)


    class Meta:
        verbose_name = _("Endereço da Escola")
        verbose_name_plural = _("Endereços da Escola")

    @property
    def get_zip_code(self):
        return self.address.zip_code
    
    @property
    def get_address(self):
        return self.address.get_type_address
    
    @property
    def get_city_state(self):
        return self.address.city.get_cityuf
    
    def __str__(self):
        return f'CEP: {self.get_zip_code} - Endereço: {self.get_address()}, {self.number}, {self.complement} - {self.get_city_state()}'


class PhoneSchool(PhoneBase):

    CELULAR = 'C'
    PRINCIPAL = 'P'
    WHATSAPP = 'W'
    TELEGRAN = 'T'
    OUTRO = 'O'
    PHONE_TYPE_CHOICES = {
        CELULAR: 'Celular',
        PRINCIPAL: 'Principal',
        WHATSAPP: 'Whatsapp',
        TELEGRAN: 'Telegran',
        OUTRO: 'Outro',
    }
    school = models.ForeignKey(
        School, 
        verbose_name=_("escola"),
        on_delete=models.CASCADE)
    phone_type = models.CharField(
        max_length=1,
        choices=PHONE_TYPE_CHOICES,
        default=PRINCIPAL,
    )

    @property
    def get_phone(self):
        prefix = ''
        if self.country_code:
            prefix = f'+{self.country_code}'
        if self.locale_code:
            prefix += f'({self.locale_code})'
        
        return f'{prefix} {self.number}'
    
    def is_upperclass(self):
        return self.phone_type in {self.CELULAR, self.PRINCIPAL}

    class Meta:
        verbose_name = _("Telefone da Escola")
        verbose_name_plural = _("Telefones da Escola")

    def __str__(self):
        return f'+{self.country_code}({self.locale_code}) {self.number}'


class TurnSchool(models.Model):

    name = models.CharField(_("Nome do Turno"), max_length=10)
    school = models.ForeignKey(
        School, 
        verbose_name=_("Escola"), 
        on_delete=models.PROTECT,
    )
    start_time = models.TimeField(_("Hora de Início"))
    duration = models.DurationField(_("Duração"))

    class Meta:
        verbose_name = _("Turno Escolar")
        verbose_name_plural = _("Turnos da Escola")

    def __str__(self):
        return self.name.title()

class ClassRoom(models.Model):
    PADRAO = 'P'
    ESPECIAL = 'E'
    INFORMATICA = 'N'
    LABORATORIO = 'L'
    INCLUSIVA = 'I'
    OUTRA = 'O'
    CLASSROOM_TYPE_CHOICES = {
        PADRAO: _('Padrão'),
        ESPECIAL: _('Especial'),
        INFORMATICA: _('Informática'),
        LABORATORIO: _('Laboratório'),
        INCLUSIVA: _('Inclusiva'),
        OUTRA: _('Outra')
    }
        
    identification = models.CharField(_("Identificação"), max_length=5)
    vacation = models.PositiveIntegerField(_("Vagas"))
    classroom_tyoe = models.CharField(
        _("Tipo de Classe de Aula"),
        max_length=1,
        choices=CLASSROOM_TYPE_CHOICES
    )
    school = models.ForeignKey(
        School,
        verbose_name=_("Escola"),
        on_delete=models.PROTECT,
    )
    class Meta:
        verbose_name = _("Sala de Aula")
        verbose_name_plural = _("Salas de Aula")

    def __str__(self):
        return f'Sala {self.identification}'


class AcademicYear(models.Model):

    start_date = models.DateField(_("Data do Inicio"))
    end_date = models.DateField(_("Data do Termino"))
    start_recess = models.DateField(_("Inicio das Férias"))
    end_recess = models.DateField(_("Final das Férias"))
    school = models.ForeignKey(
        School, 
        verbose_name=_("Escola"), 
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _("Ano Letivo")
        verbose_name_plural = _("Anos Letivos")

    def __str__(self):
        return f'Ano Letivo: {self.start_date.year}'

