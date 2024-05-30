from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth import forms 
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm 
# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect("main") # burada kontrol eder ve login sayfası gözükmez
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request, 'Account created successfully')  
            return redirect("main")    #Login olursa doğrudan indexe gider
        else:
            return render(request,"account/login.html",{"error":"username yada parola yanlis"})
          
    else:
        return render(request, "account/login.html")


def user_register(request):
    if request.method != 'POST':
        form = CustomUserForm()
       
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    context = {'form': form}

    return render(request, 'account/register.html', context)     


def user_logout(request):
     logout(request)
     return redirect( "main")