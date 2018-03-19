from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^reset$', views.reset_attempts),
    url(r'^$', views.index),
]
