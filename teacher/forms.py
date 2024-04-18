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
        fields = '__all__'
>>>>>>> ee2e9db (add, configurate and edit app teacher)
