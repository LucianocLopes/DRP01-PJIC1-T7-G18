from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'
