from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^shopping_cart$', views.index),
    url(r'^process$', views.process),
    url(r'^thank_you$', views.thank_you),
]
