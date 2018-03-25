from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^books$', views.reviews_main),
    url(r'^books/(?P<id>\d+)$', views.book_detail),
    # url(r'^users/(?P<id>\d+)$', views.user_profile),
]
