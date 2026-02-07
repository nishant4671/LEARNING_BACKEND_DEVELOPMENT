"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include # Import the include function from django.urls. This function allows you to include other URL configurations from different apps within your project.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')), # This line includes the URL patterns defined in the pages app's urls.py file. When a user visits a URL that starts with 'pages/', Django will look for the corresponding patterns in pages/urls.py to determine which view to call.
    path('', include('pages.urls')), # This line includes the URL patterns from pages/urls.py for the root URL (''). This means that when a user visits the root URL of the site, Django will look for URL patterns in pages/urls.py to determine which view to call. This allows you to set up a homepage or default landing page for your site using the views defined in the pages app
]