from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_course$', views.process_course),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^process/(?P<id>\d+)$', views.process),
]