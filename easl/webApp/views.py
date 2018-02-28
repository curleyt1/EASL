import datetime
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from .forms import StudentRegistrationForm

from .models import Student
from .models import Action

def home(request):
    students = Student.objects.all()
    return render(request, 'start_page.html', {'students': students})

def directory(request):
    students = Student.objects.all()
    return render(request, 'directory.html', {'students': students})

def registration_confirmation(request):
    students = Student.objects.all()
    return render(request, 'registration_confirmation.html', {'students': students})

def action_log(request):
    actions = Action.objects.all()
    return render(request, 'action_log.html', {'actions': actions})

def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404('Student not found')
    print('puttingactions')
    actions = Action.objects.filter(student=student)
    print(actions)
    print('done')
    return render(request, 'student_detail.html', {'student': student, 'actions': actions})

def registration_page(request):
    students = Student.objects.all()
    form = StudentRegistrationForm(request.POST)
    first_name = request.POST.get('first_name', "")
    last_name = request.POST.get('last_name', "")
    date_of_birth = request.POST.get('date_of_birth', "")
    gender = request.POST.get('gender', "")
    if form.is_valid():
        form = form.save()
    return render(request, 'registration_page.html', {'form': form})

def save_action(request, id, action_code):
    try:
        print('trying')
        acting_student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        print('failed')
        raise Http404('Student not found')
    action = Action.objects.create(time = timezone.now(), action = action_code, student = acting_student)
    actions = Action.objects.filter(student=acting_student)
    return render(request, 'student_detail.html', {'student': acting_student, 'actions': actions})

class AboutPageView(TemplateView):
    template_name = "about.html"
