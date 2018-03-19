from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^time_display$', views.index),
    url(r'^$', views.index),
]
