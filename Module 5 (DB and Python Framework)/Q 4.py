# A request in Django first comes to urls.py and then goes to the matching function in views.py. 
# Python functions in views.py take the web request from urls.py and give the web response to templates. 
# It may go to the data access layer in models.py as per the queryset.
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
]


'''from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
]'''