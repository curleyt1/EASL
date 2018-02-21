from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Student

GENDER_CHOICES = (
    ('M'),
    ('F'),
)

class StudentSelectionForm(ModelForm):
    student = forms.ModelMultipleChoiceField(queryset=Student.objects.all())

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields=('first_name', 'last_name', 'date_of_birth','gender')

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    gender = forms.Select(choices=GENDER_CHOICES)
