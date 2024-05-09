from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import City, Address, PhoneBase
from school.models import School

class Teacher(models.Model):

    first_name = models.CharField(_("Nome"), max_length=20)
    last_name = models.CharField(_("Sobrenome"), max_length=70)
    email = models.EmailField(_("E-mail"), max_length=254)
    school = models.ForeignKey(
        School, 
        verbose_name=_("Escola"), 
        on_delete=models.PROTECT,
    )

    @property
    def full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'
    
    class Meta:
        verbose_name = _("Professor(a)")
        verbose_name_plural = _("Professores")

    def __str__(self):
        return self.full_name

class AddressTeacher(models.Model):

    zipcode = models.OneToOneField(
        Address, 
        verbose_name=_("CEP"),
        on_delete=models.PROTECT
    )
    number = models.PositiveIntegerField(_("Número"))
    complement = models.CharField(_("Complemento"), max_length=20, null=True, blank=True)
    teacher = models.ForeignKey(
        Teacher, 
        verbose_name=_("Professor"),
        on_delete=models.CASCADE,
    )
    
    class Meta:
        verbose_name = _("Endereço do Professor(a)")
        verbose_name_plural = _("Endereços do Professor(a)")

    def __str__(self):
        return self.zipcode.get_address()

class PhoneTeacher(PhoneBase):

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
    teacher = models.ForeignKey(
        Teacher, 
        verbose_name=_("Professor"),
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
        verbose_name = _("Telefone do Professor(a)")
        verbose_name_plural = _("Telefones do Professor(a)")

    def __str__(self):
        return f'+{self.country_code}({self.locale_code}) {self.number}'
