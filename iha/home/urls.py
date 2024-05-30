from django.urls import path
from home.views import  main 
urlpatterns = [

    path('', main, name='main'),
       

]