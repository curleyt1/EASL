from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Student
from .models import Action
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

GENDER_CHOICES = (
    ('M'),
    ('F'),
)

ACTION_CHOICES = (
('S'),
('P'),
('O'),
('B'),
('C'),
('N'),
('R'),
)
#
# class RegistrationForm(forms.Form):
#
#     username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
#     email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
#
#     def clean_username(self):
#         try:
#             user = User.objects.get(username__iexact=self.cleaned_data['username'])
#         except User.DoesNotExist:
#             return self.cleaned_data['username']
#         raise forms.ValidationError(_("The username already exists. Please try another one."))
#
#     def clean(self):
#         if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
#             if self.cleaned_data['password1'] != self.cleaned_data['password2']:
#                 raise forms.ValidationError(_("The two password fields did not match."))
#         return self.cleaned_data
#
# from django.contrib.auth.models import User

class ParentRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=254, help_text=None)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )

class TeacherRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=254, help_text=None)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

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

class StudentEditForm(ModelForm):
    class Meta:
        model = Student
        fields=('first_name', 'last_name', 'date_of_birth','gender')

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    gender = forms.Select(choices=GENDER_CHOICES)
