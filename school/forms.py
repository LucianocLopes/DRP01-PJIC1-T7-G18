from django import forms
from django.utils.translation import gettext_lazy as _
from .models import School, StructSchool


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = '__all__'


class StructSchoolForm(forms.ModelForm):

    class Meta:
        model = StructSchool
        fields = '__all__'
