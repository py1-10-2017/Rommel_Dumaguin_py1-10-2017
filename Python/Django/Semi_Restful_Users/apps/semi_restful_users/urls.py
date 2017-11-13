from django.conf.urls import url # This gives us access to the function url
from . import views # This explicitly imports views.py from the current folder

# Uses the url method in a way that's very similar to the @app.route method in flask. The r after the ( tells Python to interpret the following as a raw string, so it won't escape any special characters -- useful when dealing with regex strings!
urlpatterns = [
    url(r'^$', views.index), # following comments are using "users" shorthand for "semi_restful_users"
    url(r'^semi_restful_users$', views.index), # render 'users/index.html'
    url(r'^semi_restful_users/new$', views.new), # render 'users/create.html'
    url(r'^semi_restful_users/create$', views.create), # if error: redirect '/users/new', else: redirect '/users'
    url(r'^semi_restful_users/(?P<user_id>\d+)$', views.show), # render 'users/show.html'
    url(r'^semi_restful_users/(?P<user_id>\d+)/edit$', views.edit), # render 'users/update.html'
    url(r'^semi_restful_users/(?P<user_id>\d+)/update$', views.update), # if error: redirect '/users/{}/edit'.format(user_id), else: redirect '/users'
    url(r'^semi_restful_users/(?P<user_id>\d+)/destroy$', views.destroy), # redirect /users
        # User.objects.get(id=user_id).delete()
]

# Have 7 routes. Because we are working with 'users', they might look like:
# GET request to /users - calls the index method to display all the users. This will need a template.
# GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template.
# GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.
# GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template.
# POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.
