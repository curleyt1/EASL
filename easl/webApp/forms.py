from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Student
from .models import Action
from django.conf import settings
# from .models import Teacher
# from .models import Parent
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

PARENT_CHOICES = User.objects.all()

ACCOUNT_TYPE=(
    ('Teacher'),
    ('Parent'),
)

class StudentSelectionForm(ModelForm):
    student = forms.ModelMultipleChoiceField(queryset=Student.objects.all())

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields=('first_name', 'last_name', 'date_of_birth', 'gender', 'parent')

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    gender = forms.Select(choices=GENDER_CHOICES)
    parent = forms.Select(choices = User.objects.all())

class StudentEditForm(ModelForm):
    class Meta:
        model = Student
        fields=('first_name', 'last_name', 'date_of_birth','gender')

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    gender = forms.Select(choices=GENDER_CHOICES)

class ParentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_staff = forms.BooleanField(initial=True, disabled=True)

    def __init__( self, *args, **kwargs ):
        super(TeacherSignUpForm, self).__init__( *args, **kwargs )
        self.fields['is_staff'].label = "" # Hide is_staff label.

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff' )
