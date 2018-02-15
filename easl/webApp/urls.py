from django.conf.urls import url
from webApp import views

urlpatterns = [
    url(r'^$', views.StartPageView.as_view()),
    url(r'^index/$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^student/(\d+)/', views.student_detail, name='student_detail'),
]
