from django.db import models
from django.utils.translation import gettext_lazy as _

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
        return f'{self.name.title()}/{self.state.get_uf}'


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