from django import forms
<<<<<<< HEAD

from .models import School


class SchoolForm(forms.ModelForm):
    
    class Meta:
        model = School
        fields = '__all__'
=======
from django.utils.translation import gettext_lazy as _
from .models import School, StructSchool


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = '__all__'


class StructSchollForm(forms.ModelForm):

    class Meta:
        model = StructSchool
        fields = '__all__'
>>>>>>> 70b58ba (add app school and config pages)
