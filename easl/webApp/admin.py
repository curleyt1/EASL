from django.contrib import admin

from .models import Student
from .models import Action

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'gender']

@admin.register(Action)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['time', 'action', 'student']
