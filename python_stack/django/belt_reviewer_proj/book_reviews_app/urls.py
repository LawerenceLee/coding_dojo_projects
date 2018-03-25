from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^books/?$', views.reviews_main),
    url(r'^books/add/?$', views.add_review),
    url(r'^books/process_review/?$', views.process_review),
    url(r'^books/process_book_and_review/?$', views.process_book_and_review),
    url(r'^books/(?P<id>\d+)/?$', views.book_detail),
    url(r'^users/(?P<id>\d+)/?$', views.user_detail),
    url(r'delete_review/(?P<id>\d+)/?$', views.delete_review),
]
