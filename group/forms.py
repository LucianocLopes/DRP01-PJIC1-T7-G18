from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Group


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
        
        exclude = ("user",)
