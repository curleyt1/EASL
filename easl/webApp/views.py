import datetime
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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
from .forms import StudentEditForm
from .forms import ParentEditForm
from .forms import StudentSelectionForm
from .forms import StudentRegistrationForm
from .forms import ParentSignUpForm
from .forms import TeacherSignUpForm
from django.contrib.auth.models import Group

from .models import Student
from .models import Action

def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            students = Student.objects.all()
            return render(request, 'start_page.html', {'students': students})
        else:
            return redirect('/parent_page')
    else:
        return redirect('/accounts/login')

def parent_signup(request):
    if request.method == 'POST':
        form = ParentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = ParentSignUpForm()
    return render(request, 'parent_signup.html', {'form': form})


def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.is_staff = True
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacher_signup.html', {'form': form})

def directory(request):
    if request.user.is_authenticated:
        students = Student.objects.all()
        return render(request, 'directory.html', {'students': students})
    else:
        return redirect('/accounts/login')

def action_log(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            actions = Action.objects.all()
            # Take list of actions and create a dictionary of action dates.
            # Each date will have a list of actions grouped into it.
            print(actions)
            actions_grouped = defaultdict(list)
            for action in actions:
                actions_grouped[action.date].append(action)
            return render(request, 'action_log.html', {'grouped_actions': sorted(actions_grouped.items())})
        else:
            return redirect('/unauth')
    else:
        return redirect('/accounts/login')

def parent_page(request):
    parent = request.user
    students = Student.objects.filter(parent=parent)
    return render(request, 'parent_page.html', {'parent': parent, 'students': students})

def student_action_log(request, id):
    if request.user.is_authenticated:
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404('Student not found')
        if request.user.is_staff or student.parent == request.user:
            actions = Action.objects.filter(student=student)
            # Take list of actions and create a dictionary of action dates.
            # Each date will have a list of actions grouped into it.
            print(actions)
            actions_grouped = defaultdict(list)
            for action in actions:
                actions_grouped[action.date].append(action)
            return render(request, 'action_log.html', {'grouped_actions': sorted(actions_grouped.items())})
        else:
            return redirect('/unauth')
    else:
        return redirect('/accounts/login')

def student_detail(request, id):
    if request.user.is_authenticated:
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404('Student not found')
        if request.user.is_staff or student.parent == request.user:
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
            actions = Action.objects.filter(student=student, time__range=(today_min, today_max))
            return render(request, 'student_detail.html', {'student': student, 'actions': actions})
        else:
            return redirect('/unauth')
    else:
        return redirect('/accounts/login')

def registration_page(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            display_success = False
            if request.method == 'POST':
                form = StudentRegistrationForm(request.POST)
                parent = User.objects.all()
                if form.is_valid():
                    first_name = request.POST.get('first_name', "")
                    last_name = request.POST.get('last_name', "")
                    date_of_birth = request.POST.get('date_of_birth', "")
                    gender = request.POST.get('gender', "")
                    parent = request.POST.get('parent', "")
                    form = form.save()
                    display_success = True
                else:
                    print(form.errors)
            form = StudentRegistrationForm()
            return render(request, 'registration_page.html', {'form': form, 'display_success': display_success})
        else:
            return redirect('/unauth')
    else:
        return redirect('/accounts/login')

def user_profile(request):
    return render(request, 'parent_page.html')

def edit_page(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
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
        else:
            return redirect('/unauth')
    else:
        return redirect('/accounts/login')

def parent_edit_page(request):
    if request.user.is_authenticated:
        parent=request.user
        display_success = False
        if request.method == 'POST':
            form = ParentEditForm(request.POST, instance=parent)
            if form.is_valid():
                first_name = request.POST.get('first_name', "")
                last_name = request.POST.get('last_name', "")
                email = request.POST.get('email', "")
                form.save()
                display_success = True
        form = ParentEditForm(initial={
            'first_name': parent.first_name,
            'last_name': parent.last_name,
            'email': parent.email
            })
        return render(request, 'parent_edit_page.html', {'form': form, 'display_success': display_success})
    else:
        return redirect('/accounts/login')

def save_action(request, id, action_code):
    if request.user.is_authenticated:
        if request.user.is_staff:
            try:
                acting_student = Student.objects.get(id=id)
            except Student.DoesNotExist:
                raise Http404('Student not found')
            action = Action.objects.create(time = timezone.now(), action = action_code, student = acting_student)
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
            actions = Action.objects.filter(student=acting_student, time__range=(today_min, today_max))

            #return render(request, 'student_detail.html', {'student': acting_student, 'actions': actions})
            return redirect('/student/' + str(id))
        else:
            return redirect('/unauth')
    else:
        return redirect('/accounts/login')


# TODO: re-create as a post form to validate with CSRF
def delete_student(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            try:
                student = Student.objects.get(id=id)
                student.delete()
            except Student.DoesNotExist:
                raise Http404('Student not found')
            students = Student.objects.all()
            return render(request, 'start_page.html', {'students': students})
        else:
            return redirect('/unauth')
    else:
        return redirect('/accounts/login')

class unauthorized(TemplateView):
    template_name = "unauthorized.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
class user_guide(TemplateView):
    template_name = "user_guide.html"
