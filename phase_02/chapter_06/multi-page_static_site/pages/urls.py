from django.urls import path # this is used to define urls for our application , we will use this to define urls for home page , about page and contact page
from . import views # this is used to import views from current directory which is pages , we will use this to call view functions for home page , about page and contact page in urls.py file

urlpatterns = [ # this is the list of urls for our application , we will define urls for home page , about page and contact page in this list
    path('', views.home, name='home'),# this is the url for home page which will call home view function when we access this url in the browser
    path('about/', views.about, name='about'),# this is the url for about page which will call about view function when we access this url in the browser
    path('contact/', views.contact, name='contact'), # this is the url for contact page which will call contact view function when we access this url in the browser
]




# syntax of the urlpatterns here 
# urlpatterns = [
#     path('url/', views.view_function, name='url_name'),
# ]
# # flowchart of the code here is as follows:
# # what is happeneing here
# # 1. we are importing path from django.urls and views from current directory which is pages
# # 2. we are defining urlpatterns which is a list of urls for our application
# # 3. we are defining three urls for home page , about page and contact page which will call respective view functions when we access these urls in the browser
