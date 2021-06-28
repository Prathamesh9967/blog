from django.shortcuts import render , redirect , get_object_or_404
from .models import Carousal , cards 
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User , auth

# Create your views here.

def index(request):
    obj =  Carousal.objects.all()

    queryset = cards.objects.filter(trending=True)

    return render(request , 'index.html' , {'obj':obj , 'queryset':queryset ,})

def readmore(request , id):
    if request.user.is_authenticated:
        card = get_object_or_404(cards , id=id)
        return render(request , 'readmore.html' , {'card':card})    
    else:
        return redirect("login")          

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.success(request , "Username is taken . Please enter another username.")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.success(request , "Email is taken . Please enter another one.")
            return redirect('register')
        else:        
            user = User.objects.create_user(first_name=first_name , last_name=last_name , username=username , email=email , password=password)
            user.save()
            messages.success(request , "your registration has been done succesfully")
            return redirect("login")


    else:
        return render(request , 'register.html')    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)

        if user is not None:
            auth.login(request , user)
            return redirect("/")
        else:
            messages.success(request , "Invalid Credentials")
            return redirect("login") 
    else:           
        return render(request , 'login.html')    

def logout(request):
    auth.logout(request)
    return redirect("/")            


def blog(request):
    card = cards.objects.all()
    return render(request , 'blog.html' , {"card":card})   
