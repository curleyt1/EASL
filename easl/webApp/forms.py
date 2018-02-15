from django.db import models
from django.forms import ModelForm
#from django import forms
from .models import Student

class StudentSelectionForm(ModelForm):
    student = forms.ModelMultipleChoiceField(queryset=Student.objects.all())
