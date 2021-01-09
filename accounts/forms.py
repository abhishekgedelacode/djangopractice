from django import forms
from django.forms import fields
from .models import Student


class Stdform(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'id_no',
        ]
