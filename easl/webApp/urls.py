from django.conf.urls import url
from webApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^student/(\d+)/([A-Z])/', views.save_action, name='save_action'),
    url(r'^student/(\d+)/', views.student_detail, name='student_detail'),
    url(r'registration_page', views.registration_page, name='registration_page'),
    url(r'^actions/$', views.action_log, name='action_log'),
    url(r'^directory/$', views.directory, name='directory'),

]
