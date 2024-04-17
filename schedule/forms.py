from django import forms
from django.utils.translation import gettext_lazy as _
from .models import CalendarEvent


class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = '__all__'
