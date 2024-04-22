from django.db import models
from django.utils.translation import gettext_lazy as _
<<<<<<< HEAD
<<<<<<< HEAD

from django.urls import reverse


class State(models.Model):

    name = models.CharField(_("Nome do Estado"), max_length=50)
    acronym = models.CharField(_("Sigla do Estado"), max_length=2)

    class Meta:
        verbose_name = _("Estado")
        verbose_name_plural = _("Estados")

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse("State_detail", kwargs={"pk": self.pk})
    
    def get_uf(self):
        return self.acronym.upper()


class City(models.Model):

    name = models.CharField(_("Nome da Cidade"), max_length=50)
    ibge_number = models.CharField(_("Código do IBGE"), max_length=10)
    state = models.ForeignKey(
        State, 
        verbose_name=_("Estado"),
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _("Cidade")
        verbose_name_plural = _("Cidades")

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse("City_detail", kwargs={"pk": self.pk})

    def get_cityuf(self):
        return f'{self.name.title()}/{self.state.get_uf()}'


class AddressType(models.Model):

    name = models.CharField(_("Tipo de Endereço"), max_length=15)

    class Meta:
        verbose_name = _("Tipo de Endereço")
        verbose_name_plural = _("Tipos de Endereço")

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse("AddressType_detail", kwargs={"pk": self.pk})


class Address(models.Model):

    zip_code = models.CharField(_("CEP"), max_length=8, unique=True)
    address_type = models.ForeignKey(
        AddressType, 
        verbose_name=_("Tipo de Lougradouro"),
        on_delete=models.PROTECT,
    )
    address = models.CharField(_("Endereço"), max_length=100)
    district = models.CharField(_("Bairro"), max_length=40)
    city = models.ForeignKey(
        City, 
        verbose_name=_("Cidade"), 
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _("Endereço")
        verbose_name_plural = _("Endereços")

    def __str__(self):
        return self.zip_code

    def get_absolute_url(self):
        return reverse("Address_detail", kwargs={"pk": self.pk})

    def get_address(self):
        return f'{self.zip_code} - {self.address_type} {self.address.title()} - {self.district.title()} - {self.city.get_cityuf}'
    
    def get_type_address(self):
        return f'{self.address_type} {self.address}'

class PhoneBase(models.Model):

    country_code = models.IntegerField(_("Código do Pais"))
    locale_code = models.IntegerField(_("Código da Localidade"))
    number = models.IntegerField(_("Numero"))

    class Meta:
        abstract = True
=======
=======

>>>>>>> 8b7b00c (corrections in apps views, forms and templates)
from django.contrib.auth import get_user_model

USER = get_user_model()


# CHOICES
class Lougradouro_Choice(models.TextChoices):
    AIRPORT = "AIP", _("Aeroporto")
    ALAMEDA = "ALD", _("Alameda")
    AREA = "ARE", _("Área")
    AVENIDA = "AVE", _("Avenida")
    CAMPO = "CAP", _("Campo")
    CHACARA = "CHA", _("Chácara")
    COLONIA = "COL", _("Colônia")
    CONDOMINIO = "COD", _("Condomínio")
    CONJUNTO = "CJT", _("Conjunto")
    DISTRITO = "DIS", _("Distrito")
    ESPLANADA = "ESP", _("Esplanada")
    ESTACAO = "EST", _("Estação")
    ESTRADA = "ESD", _("Estrada")
    FAVELA = "FAV", _("Favela")
    FAZENDA = "FAZ", _("Fazenda")
    FEIRA = "FEI", _("Feira")
    JARDIM = "JAD", _("Jardim")
    LADEIRA = "LAD", _("Ladeira")
    LAGO = "LAG", _("Lago")
    LAGOA = "LGO", _("Lagoa")
    LARGO = "LRG", _("Largo")
    LOTEAMENTO = "LOT", _("Loteamento")
    MORRO = "MOR", _("Morro")
    NUCLEO = "NUC", _("Núcleo")
    PARQUE = "PAR", _("Parque")
    PASSARELA = "PAS", _("Passarela")
    PATIO = "PAT", _("Pátio")
    PRACA = "PRA", _("Praça")
    QUADRA = "QUA", _("Quadra")
    RECANTO = "REC", _("Recanto")
    RESIDENCIAL = "RES", _("Residencial")
    RODOVIA = "ROD", _("Rodovia")
    RUA = "RUA", _("Rua")
    SETOR = 'SET', _("Setor")
    SITIO = 'SIT', _("Sítio")
    TRAVESSA = 'TRA', _("Travessa")
    TRECHO = 'TRE', _("Trecho")
    TREVO = 'TRV', _("Trevo")
    VALE = 'VAL', _("Vale")
    VEREDA = 'VER', _("Vereda")
    VIA = 'VIA', _("Via")
    VIADUTO = 'VDT', _("Viaduto")
    VIELA = 'VIE', _("Viela")
    VILA = 'VIL', _("Vila")


# ABSTRACT MODELS
class TimeStamp(models.Model):
    create = models.DateTimeField(
        _("criado em"), auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(
        _("modificado em"), auto_now=True, auto_now_add=False)
    user = models.ForeignKey(USER, verbose_name=_(
        "Usuário"), on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class AddressBase(TimeStamp):
    zip_code = models.CharField(_("CEP"), max_length=8)
    type_lougradouro = models.ForeignKey(
        "Lougradouro", verbose_name=_("Tipo de Lougradouro"),
        on_delete=models.DO_NOTHING
    )
    adrress = models.CharField(_("Endereço"), max_length=100)
    district = models.CharField(_("Bairro"), max_length=50)
    cidade = models.ForeignKey(
        "cidade", verbose_name=_("Cidade"), on_delete=models.DO_NOTHING)


# MODELS
class Lougradouro(TimeStamp):
    name = models.CharField(_("Tipo de Lougradouro"), max_length=50)

    class Meta:
        """Meta definition for Lougradouro."""

        verbose_name = 'Lougradouro'
        verbose_name_plural = 'Lougradouros'

    def __str__(self):
        """Unicode representation of Lougradouro."""
        return self.name.title()


class Estado(TimeStamp):
    name = models.CharField(_("Estado"), max_length=50)
    abbreviaton = models.CharField(_("Abreviacao"), max_length=2)

    class Meta:
        """Meta definition for Estado."""

        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        """Unicode representation of Estado."""
        return f'{self.name.title()}/{self.abbreviaton.upper()}'

    def get_uf(self):
        return self.abbreviation.upper()


class Cidade(TimeStamp):
    name = models.CharField(_("Cidade"), max_length=50)
    estado = models.ForeignKey(
        Estado,
        verbose_name=_("UF"),
        on_delete=models.CASCADE
    )

    class Meta:
        """Meta definition for Cidade."""

        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        """Unicode representation of Cidade."""
        return f'{self.name.title()} - {self.estado}'
>>>>>>> a8c0174 (include core app and configs)
