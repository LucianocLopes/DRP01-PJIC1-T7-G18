from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        
        exclude = ('user',)
