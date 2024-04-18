<<<<<<< HEAD
from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Address, PhoneBase

from .utils import weeks, number_week, days_week

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


class SchoolYear(models.Model):
    school = models.ForeignKey(
        School, 
        verbose_name=_("Escola"), 
        on_delete=models.CASCADE
    )
    first_start = models.DateField(_("Inicio ano letivo"))
    halfyear_start = models.DateField(_("Inicio Ferias"))
    second_start = models.DateField(_("Inicio 2º Semestre"))
    end = models.DateField(_("Termino ano letivo"), auto_now=False, auto_now_add=False)

    @property
    def first_semester(self) -> dict:
        start = datetime(year=self.first_start.year, month=self.first_start.month, day=self.first_start.day)
        end = datetime(year=self.halfyear_start.year,month=self.halfyear_start.month,day=self.halfyear_start.day)
        
        n_week = sorted(number_week(weeks(start, end)))
        dict = {
            'start': start,
            'end': end,
            'weeks': list(n_week),
        }
        return dict
    
    
    @property
    def second_semester(self) -> dict:
        start = datetime(year=self.second_start.year, month=self.second_start.month, day=self.second_start.day)
        end = datetime(year=self.end.year,month=self.end.month,day=self.end.day)
        
        n_week = sorted(number_week(weeks(start, end)))
        dict = {
            'start': start,
            'end': end,
            'weeks': list(n_week),
        }
        return dict
    
    
        
    class Meta:
        verbose_name = _("Ano Letivo")
        verbose_name_plural = _("Anos Letivos")

    def __str__(self):
        return f'Ano: {self.first_start.year}'
    
    
=======
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
>>>>>>> 70b58ba (add app school and config pages)
