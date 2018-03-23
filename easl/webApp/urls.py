from django.conf.urls import url
from django.contrib.auth.views import login
from webApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^student/(\d+)/([A-Z])/', views.save_action, name='save_action'),
    url(r'^student/(\d+)/', views.student_detail, name='student_detail'),
    url(r'parent_page', views.parent_page, name='parent_page'),
    url(r'edit_page/(\d+)/', views.edit_page, name='edit_page'),
    url(r'^delete/(\d+)/', views.delete_student, name='delete_student'),
    url(r'^actions/$', views.action_log, name='action_log'),
    url(r'^actions/(\d+)/', views.student_action_log, name='student_action_log'),
    url(r'^directory/$', views.directory, name='directory'),
]
