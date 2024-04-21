from django import forms
from django.contrib.admin import widgets as admin_widgets
from django.utils.translation import gettext_lazy as _

from .models import CalendarEvent


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

    class Meta:
        model = CalendarEvent
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(CalendarEventForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.atrs['class'] = 'form-control'
