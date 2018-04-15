from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Student
from .models import Action
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


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

VALID_DOMAINS = (
    ('gmail.com'),
    ('wit.edu'),
    ('mit.edu'),
    ('northeastern.edu'),
    ('yahoo.com'),
    ('yahoo.ca'),
    ('hotmail.com'),
    ('hotmail.co.uk'),
    ('hotmail.fr'),
    ('comcast.net'),
    ('outlook.com'),
    ('aol.com'),
    ('verizon.net'),
    ('protonmail.ch'),
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
        fields=('first_name', 'last_name', 'date_of_birth','gender', 'parent')

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    gender = forms.Select(choices=GENDER_CHOICES)
    parent = forms.Select(choices = User.objects.all())

class ParentEditForm(ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ParentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = models.EmailField(max_length=254, blank=False, unique=True, help_text='Required. Inform a valid email address.', validators=[validate_email])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        domain = email.split('@')[1]
        if domain not in VALID_DOMAINS:
            raise ValidationError('\"' + domain + '\"' + ' does not appear to be a valid domain.')

class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = models.EmailField(max_length=254, blank=False, unique=True, help_text='Required. Inform a valid email address.', validators=[validate_email])
    is_staff = forms.BooleanField(initial=True, disabled=True)

    def __init__( self, *args, **kwargs ):
        super(TeacherSignUpForm, self).__init__( *args, **kwargs )
        self.fields['is_staff'].label = "" # Hide is_staff label.

    class Meta:
        model = User
        fields = ('is_staff', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        domain = email.split('@')[1]
        if domain not in VALID_DOMAINS:
            raise ValidationError('\"' + domain + '\"' + ' does not appear to be a valid domain.')
