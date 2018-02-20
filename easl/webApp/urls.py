from django.conf.urls import url
from webApp import views

urlpatterns = [
    url(r'^$', views.StartPageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^home/$', views.home, name='home'),
    url(r'^student/(\d+)/', views.student_detail, name='student_detail'),
    url(r'registration_page', views.registration_page, name='registration_page')
]
