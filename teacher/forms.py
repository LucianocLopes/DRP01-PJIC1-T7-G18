from django.http import request
from django import forms
<<<<<<< HEAD
=======
from django.utils.translation import gettext_lazy as _
>>>>>>> ee2e9db (add, configurate and edit app teacher)

from .models import Teacher


class TeacherForm(forms.ModelForm):
<<<<<<< HEAD
    
    class Meta:
        model = Teacher
        fields = '__all__'
    
    
=======

    class Meta:
        model = Teacher
<<<<<<< HEAD
        fields = '__all__'
>>>>>>> ee2e9db (add, configurate and edit app teacher)
=======
        fields = ['school', 'first_name', 'last_name', 'email', 'phone_ddd', 'phone_number', 'address_zipcode',
                  'address', 'address_number', 'address_complement', 'address_district', 'address_city', 'address_state']
>>>>>>> 8b7b00c (corrections in apps views, forms and templates)
