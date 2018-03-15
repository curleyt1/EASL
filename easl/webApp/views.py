import datetime
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from .forms import StudentRegistrationForm
from .forms import StudentEditForm

from .models import Student
from .models import Action
from .models import Parent

def home(request):
    students = Student.objects.all()
    return render(request, 'start_page.html', {'students': students})

def directory(request):
    students = Student.objects.all()
    return render(request, 'directory.html', {'students': students})

def action_log(request):
    actions = Action.objects.all()
    return render(request, 'action_log.html', {'actions': actions})


def parent_page(request):
    parents = Parent.objects.all()
    return render(request, 'parent_page.html', {'parents': parents})


def student_action_log(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404('Student not found')
    actions = Action.objects.filter(student=student)
    return render(request, 'action_log.html', {'actions': actions})

def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404('Student not found')
    print('puttingactions')
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    actions = Action.objects.filter(student=student, time__range=(today_min, today_max))
    return render(request, 'student_detail.html', {'student': student, 'actions': actions})

def registration_page(request):
    display_success = False
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get('first_name', "")
            last_name = request.POST.get('last_name', "")
            date_of_birth = request.POST.get('date_of_birth', "")
            gender = request.POST.get('gender', "")
            form = form.save()
            display_success = True
    form = StudentRegistrationForm()
    return render(request, 'registration_page.html', {'form': form, 'display_success': display_success})

def edit_page(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404('Student not found')
    display_success = False
    if request.method == "POST":
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            first_name = request.POST.get('first_name', "")
            last_name = request.POST.get('last_name', "")
            date_of_birth = request.POST.get('date_of_birth', "")
            gender = request.POST.get('gender', "")
            form = form.save()
            display_success = True
    form = StudentEditForm(initial={
            'first_name': student.first_name,
            'last_name': student.last_name,
            'date_of_birth': student.date_of_birth,
            'gender': student.gender
            })
    return render(request, 'edit_page.html',{'student': student, 'form': form, 'display_success': display_success})

def save_action(request, id, action_code):
    try:
        acting_student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404('Student not found')
    action = Action.objects.create(time = timezone.now(), action = action_code, student = acting_student)
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    actions = Action.objects.filter(student=acting_student, time__range=(today_min, today_max))
    return render(request, 'student_detail.html', {'student': acting_student, 'actions': actions})

# TODO: re-create as a post form to validate with CSRF
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
    except Student.DoesNotExist:
        raise Http404('Student not found')
    students = Student.objects.all()
    return render(request, 'start_page.html', {'students': students})

class AboutPageView(TemplateView):
    template_name = "about.html"
