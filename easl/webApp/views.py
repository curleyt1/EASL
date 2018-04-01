import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth import authenticate
from django.forms import ModelForm
from django.contrib.auth import login
from .forms import ParentRegistrationForm
from .forms import TeacherRegistrationForm
from .forms import StudentEditForm
from .forms import StudentSelectionForm
from .forms import StudentRegistrationForm
from .forms import ParentLoginForm
from django.contrib.auth.models import Group


from .models import Student
from .models import Action

# @csrf_protect
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password1'],
#             email=form.cleaned_data['email']
#             )
#             return HttpResponseRedirect('/register/success/')
#     else:
#         form = RegistrationForm()
#     variables = RequestContext(request, {
#     'form': form
#     })
#
#     return render_to_response(
#     'registration/register.html',
#     variables,
#     )
#
# def register_success(request):
#     return render_to_response(
#     'registration/success.html',
#     )

# def logout_page(request):
#     logout(request)
#     return HttpResponseRedirect('/')
#
# @login_required
# def home(request):
#     students = Student.objects.all()
#     return render_to_response(
#     'start_page.html',
#     { 'user': request.user, 'students': students }
#     )

def home(request):
    students = Student.objects.all()
    return render(request, 'start_page.html', {'students': students})

def parent_login(request):
    if request.method == 'POST':
        form = ParentLoginForm(request.POST)
        if form.is_valid():
            form = form.save(ModelForm)
    form = ParentLoginForm(ModelForm)
    return render(request, 'registration/parent_login.html', {'form': form })

def teacher_login(request):
    return render(request, 'registration/teacher_login.html')

def directory(request):
    students = Student.objects.all()
    return render(request, 'directory.html', {'students': students})

def action_log(request):
    actions = Action.objects.all()
    return render(request, 'action_log.html', {'actions': actions})


def parent_page(request, id):
    parents = Parent.objects.get(id=id)
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

def user_profile(request):
    return render(request, 'parent_page.html')

def parent_registration(request):
    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/parent_registration.html', {'form': form})
    else:
        form = ParentRegistrationForm()
    return render(request, 'registration/parent_registration.html', {'form': form})

def teacher_registration(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/teacher_registration.html', {'form': form})
    else:
        form = TeacherRegistrationForm()
    return render(request, 'registration/teacher_registration.html', {'form': form})


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
