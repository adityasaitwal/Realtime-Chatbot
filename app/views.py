from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from app.models import Message
from . forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def Home(request):
    return render(request,"first.html")

def Second(request):
    return render(request,"second.html")

def SignUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(SignUpDone)
    else:
        form = SignUpForm()
    return render(request,"signup.html",{"form":form})

def SignUpDone(request):
    return HttpResponse("<h1>Success! Your Account is Created, Please Login!</h1>")





