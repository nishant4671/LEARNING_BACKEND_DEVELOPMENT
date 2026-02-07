# pages/urls.py
from django.urls import path #import the path function from django.urls module. This function is used to define URL patterns for the application.
from . import views # Import the views module from the current package (indicated by .). This allows us to reference the view functions defined in views.py when we set up our URL patterns.


urlpatterns = [ # Define a list of URL patterns for the application. Each pattern is created using the path function, which takes a URL pattern, a view function to handle requests to that pattern, and an optional name for the pattern.
    path('', views.home, name='home'), # This pattern matches the root URL ('') and maps it to the home view function defined in views.py. The name 'home' can be used to refer to this URL pattern elsewhere in the application (e.g., in templates or other views).
]