from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


def register(request):
    if request.POST:  
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        if password == confirm_password:
            new_user = User.objects.create(username=username,password=make_password(password),email=email,phone_number=phone_number,address=address)
            messages.success(request, 'User registered Successfully')
            print("suc")
            return redirect('/login')
        else:
            messages.error(request, 'Password and confirm password not matched.!')
            return render(request, 'register.html')

    print("else")
    return render(request, 'register.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        print(user,"user")
        if user is not None:
            login(request, user)
            messages.success(request, 'User login Successfully')
            return redirect('/')
        else:
            messages.error(request,'Error')
            return render(request, 'login.html',{'message':"Invalid Credentials"})
    return render(request, 'login.html')

