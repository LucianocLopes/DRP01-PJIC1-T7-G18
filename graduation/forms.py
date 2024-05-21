from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Discipline, Graduation


class DisciplineForm(forms.ModelForm):

    class Meta:
        model = Discipline
        fields = '__all__'


class GraduationForm(forms.ModelForm):

    class Meta:
        model = Graduation
        fields = '__all__'
