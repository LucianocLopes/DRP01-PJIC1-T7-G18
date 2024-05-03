from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Discipline, Graduation


class DisciplineForm(forms.ModelForm):

    class Meta:
        model = Discipline
        fields = ['name', 'duration']


class GraduationForm(forms.ModelForm):

    class Meta:
        model = Graduation
        fields = '__all__'
        exclude = ('user',)
        # widgets = {'user': forms.HiddenInput()}
