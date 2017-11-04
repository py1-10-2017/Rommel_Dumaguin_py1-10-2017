from django.conf.urls import url # This gives us access to the function url
from . import views # This explicitly imports views.py from the current folder

urlpatterns = [
    url(r'^$', views.index), # Uses the url method in a way that's very similar to the @app.route method in flask. The r after the ( tells Python to interpret the following as a raw string, so it won't escape any special characters -- useful when dealing with regex strings!
    url(r'^surveys/process$', views.process),
    url(r'^result$', views.result),
    url(r'^logoff$', views.logoff),
]
