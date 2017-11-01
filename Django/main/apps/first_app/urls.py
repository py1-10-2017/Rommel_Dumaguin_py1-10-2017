from django.conf.urls import url # This gives us access to the function url
from . import views           # This line is new! This explicitly imports views.py in the current folder.

urlpatterns = [
    url(r'^$', views.index)     # This line has changed! Uses the url method in a way that’s very similar to the @app.route method in flask. The r after the ( tells Python to interpret the following as a raw string, so it won't escape any special characters -- useful when dealing with regex strings! 
]
