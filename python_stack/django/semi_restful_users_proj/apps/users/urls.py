from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new$', views.new_user, name="new"),
    url(r'^create$', views.create_user, name="create"),
    url(r'^(?P<id>\d+)$', views.user_by_id, name="user"),
    url(r'^(?P<id>\d+)/edit', views.edit_user, name="edit"),
    url(r'^(?P<id>\d+)/update', views.update_user, name="update"),
    url(r'^(?P<id>\d+)/delete$', views.delete_user, name="delete"),
]
