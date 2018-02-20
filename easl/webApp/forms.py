from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Student

class StudentSelectionForm(ModelForm):
    student = forms.ModelMultipleChoiceField(queryset=Student.objects.all())

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields=('first_name', 'last_name', 'date_of_birth',)

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    #gender = forms.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
