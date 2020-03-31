from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import  User,auth


def logout(request):
    auth.logout(request)
    return redirect('/')
    
def login(request) :
    if request.method=="POST" :

        username=request.POST['uname']
        password=request.POST['pword']

        user=auth.authenticate(username=username,password=password)
        if user is not None :
           auth.login(request,user)
           return redirect('/')
        else :
            messages.info(request,"Invalid creds")
            return redirect('login')

    else :
        return render(request,'login.html')

def register(request) :
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
        user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.save()
        return redirect('login')
    else :
        return render(request,"register.html")
