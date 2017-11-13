from django.conf.urls import url # This gives us access to the function url
from . import views # This explicitly imports views.py from the current folder

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.index), # render 'courses/index.html'
    url(r'^courses/create$', views.create), # if error: redirect '/courses/new', else: redirect '/courses'
    url(r'^courses/(?P<course_id>\d+)/confirm_destroy$', views.confirm_destroy),
    url(r'^courses/(?P<course_id>\d+)/destroy$', views.destroy), # redirect /courses
]
