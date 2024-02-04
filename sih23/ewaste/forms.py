from django import forms
from .models import storelogin

class storeform(forms.ModelForm):
    class Meta:
        model = storelogin
        fields = '__all__'
