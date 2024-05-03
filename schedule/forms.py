from django import forms
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.admin import widgets as admin_widgets
=======
>>>>>>> ac9891b (corrections apps)
=======
from django.contrib.admin import widgets as admin_widgets
>>>>>>> 98c1c6d (corrects on apps)
from django.utils.translation import gettext_lazy as _
from .models import CalendarEvent


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d22ecf1 (correctons apps school. schedule, core)


class AdminSplitDateTime(admin_widgets.AdminSplitDateTime):
    def __init__(self, attrs: dict[str, str] | None = ..., date_format: str | None = ..., time_format: str | None = ..., date_attrs: dict[str, str] | None = ..., time_attrs: dict[str, str] | None = ...) -> None:
        super().__init__(attrs, date_format, time_format, date_attrs, time_attrs)

class CalendarEventForm(forms.ModelForm):
    start = forms.SplitDateTimeField(widget=admin_widgets.AdminSplitDateTime(), label='Iniciando em')
    end = forms.SplitDateTimeField(widget=admin_widgets.AdminSplitDateTime(), label='Terminando em')

<<<<<<< HEAD
=======
class CalendarEventForm(forms.ModelForm):
>>>>>>> ac9891b (corrections apps)
=======
class CustomAdminSplitDateTime(admin_widgets.AdminSplitDateTime):

    def __init__(self, attrs=None):
        widgets = [admin_widgets.AdminDateWidget(
            attrs={'type': 'date'}, format='%Y-%m-%d'), admin_widgets.AdminTimeWidget(attrs={'type': 'time'}, format='%H:%M')]
        forms.MultiWidget.__init__(self, widgets, attrs)


class CalendarEventForm(forms.ModelForm):
    required_css_class = 'required'

    title = forms.CharField(
        label='Titulo do Evento'
    )

    start = forms.DateTimeField(
        label='Inicia',
        widget=CustomAdminSplitDateTime(
        ),
    )

    end = forms.DateTimeField(
        label='Termina',
        widget=CustomAdminSplitDateTime(
        ),
    )

    all_day = forms.BooleanField(
        label='Todo o Dia',
        widget=forms.CheckboxInput()
    )

>>>>>>> 98c1c6d (corrects on apps)
=======
class CalendarEventForm(forms.ModelForm):
>>>>>>> 8b7b00c (corrections in apps views, forms and templates)
=======
>>>>>>> d22ecf1 (correctons apps school. schedule, core)
    class Meta:
        model = CalendarEvent
        fields = '__all__'
