from django.shortcuts import render  #this is not used in the current code but we will use this in the future when we will render templates , but for now we will just return simple httpresponse for each page , example of templates are home.html , about.html and contact.html which we will create in the future when we will learn about templates in django

from django.http import HttpResponse # this is used to return simple httpresponse for each page , example of httpresponse are home page , about page and contact page which we will create in the future when we will learn about templates in django

def home(request): # this is the view function for home page which will return simple httpresponse for home page
    return HttpResponse("Home Page")

def about(request):# this is the view function for about page which will return simple httpresponse for about page
    return HttpResponse("About Page")

def contact(request): # this is the view function for contact page which will return simple httpresponse for contact page
    return HttpResponse("Contact Page")




# # flowchart of th code here is as follows:
# what is happeneing here 
# 1. we are importing render and HttpResponse from django.shortcuts and django.http respectively
# 2. we are defining three view functions home , about and contact which will return simple httpresponse for each page
# 3. we will create urls for each page in urls.py file and then we will run the server and test the urls in the browser to see the output of each page
    