from django import forms
from django.contrib.admin import widgets as admin_widgets
from django.utils.translation import gettext_lazy as _

from .models import CalendarEvent


class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = '__all__'

        widgets = {
            'start': admin_widgets.AdminSplitDateTime(),
            'end': admin_widgets.AdminSplitDateTime(),
        },
        labels = {
            'start': _('Iniciando em:'),
            'event_end': _('Terminando em:'),
        },
        field_classes = {
            'start': forms.SplitDateTimeField,
            'end': forms.SplitDateTimeField,

        }
