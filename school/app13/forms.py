from django import forms
from app13.models import Register
from app13.models import School

class Newform(forms.ModelForm):
    class Meta():
        model=Register
        fields="__all__"

class Newsh(forms.ModelForm):
    class Meta():
        model=School
        fields="__all__"         


        