from django.conf.urls import url # This gives us access to the function url
from . import views # This explicitly imports views.py from the current folder

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^logoff$', views.logoff),
    url(r'^delete$', views.delete),
]
