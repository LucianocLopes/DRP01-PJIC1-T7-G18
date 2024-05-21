from django import forms
from django.contrib.admin import widgets as admin_widgets
from django.utils.translation import gettext_lazy as _
from .models import CalendarEvent




class AdminSplitDateTime(admin_widgets.AdminSplitDateTime):
    def __init__(self, attrs: dict[str, str] | None = ..., date_format: str | None = ..., time_format: str | None = ..., date_attrs: dict[str, str] | None = ..., time_attrs: dict[str, str] | None = ...) -> None:
        super().__init__(attrs, date_format, time_format, date_attrs, time_attrs)

class CalendarEventForm(forms.ModelForm):
    start = forms.SplitDateTimeField(widget=admin_widgets.AdminSplitDateTime(), label='Iniciando em')
    end = forms.SplitDateTimeField(widget=admin_widgets.AdminSplitDateTime(), label='Terminando em')

    class Meta:
        model = CalendarEvent
        fields = '__all__'
