from django import forms
<<<<<<< HEAD

from .models import Group, GridGroup


class GroupForm(forms.ModelForm):
    
    class Mete:
        model: Group
        fields = '__all__'


class GridGroupForm(forms.ModelForm):
    
    class Meta:
        model = GridGroup
        fields = '__all__'
=======
from django.utils.translation import gettext_lazy as _

from .models import Group


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
<<<<<<< HEAD

        widgets = {'user': forms.HiddenInput()}
>>>>>>> 93b9589 (add and config new app group)
=======
>>>>>>> d22ecf1 (correctons apps school. schedule, core)
