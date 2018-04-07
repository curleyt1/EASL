from datetime import date
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    parent = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def age(self):
        today = date.today()

        try:
            birthday = self.date_of_birth.replace(year=today.year)
        except ValueError:
            birthday = self.date_of_birth.replace(year=today.year)

        if birthday > today:
            return today.year - self.date_of_birth.year - 1
        else:
            return today.year - self.date_of_birth.year

    def __str__(self):
        return(self.first_name + ' ' + self.last_name)

    class Meta:
        unique_together = [("first_name", "last_name", "date_of_birth")]
        ordering = ['last_name']

class Action(models.Model):
    ACTION_CHOICES = [('S', 'Snack'), ('P', 'Play'), ('O', 'Outside'), ('B', 'Bathroom'), ('C', 'CallHome'), ('N', 'Nurse'), ('R', 'Read')]
    time = models.DateTimeField()
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-time']
