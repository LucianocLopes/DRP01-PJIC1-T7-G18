from django.http import request
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['school', 'first_name', 'last_name', 'email', 'phone_ddd', 'phone_number', 'address_zipcode',
                  'address', 'address_number', 'address_complement', 'address_district', 'address_city', 'address_state']
