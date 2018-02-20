from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import Http404
from .forms import StudentRegistrationForm

from .models import Student

#class StartPageView(TemplateView):
#    students = Student.objects.all()
#    template_name = "start_page.html"

def start_page(request):
    students = Student.objects.all()
    return render(request, 'start_page.html', {'students': students})

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404('Student not found')
    return render(request, 'student_detail.html', {'student': student})

def registration_page(request):
    students = Student.objects.all()
    form = StudentRegistrationForm()
    return render(request, 'registration_page.html', {'form': students})

class AboutPageView(TemplateView):
    template_name = "about.html"
