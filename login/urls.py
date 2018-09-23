from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student_login/$', views.student, name='student'),
    url(r'^teacher_login/$', views.teacher, name='teacher'),
    url(r'^student_upload/$', views.student_upload, name='student_upload'),
    url(r'^teacher_upload/$', views.teacher_upload, name='teacher_upload'),
]