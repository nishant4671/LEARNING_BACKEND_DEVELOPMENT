from django.shortcuts import render 

from django.http import HttpResponse  # Import HttpResponse class - needed to return text/HTML

def home(request):#here we ahve defined a function called home that takes in a request object as a parameter . The request object contains information about the incoming HTTP request, such as the method (GET, POST, etc.), headers, and any data sent by the client.
    """A simple view that returns 'Home Page' as plain text"""
    return HttpResponse("Home Page")


# Create your views here.

# views.py is the core file where you define the logic that handles HTTP requests and returns HTTP responses. It's the "controller" in Django's MVT (Model-View-Template) pattern.







# What Views Do:
# Handle HTTP requests (GET, POST, PUT, DELETE)

# Process data (form submissions, user input, database queries)

# Return responses (HTML pages, JSON data, redirects)

# Connect URLs to logic (via urls.py)

# User visits URL → urls.py (routes) → views.py (processes) → Response
#        ↓                ↓                   ↓
#     Browser        Which view?         What to do?
#                                      • Query DB
#                                      • Process form
#                                      • Render template
#                                      • Return JSON/redirect


