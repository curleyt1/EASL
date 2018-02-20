from datetime import date
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])

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

