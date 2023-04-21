from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import profile
from django.contrib.auth.models import User

# Create your views here.
def route(request):
    return render(request,'landing.html')

def register(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        name=request.POST.get("name")
        email=request.POST.get("email")
        p1=request.POST.get("p1")
        p2=request.POST.get("p2")
        line1=request.POST.get("line1")
        city=request.POST.get("city")
        state=request.POST.get("state")
        pin=request.POST.get("pincode")
        pp=request.FILES.get("pp")
        address=line1+','+city+','+state+','+pin
        if p1!=p2:
            messages.error(request,"passwords dont match")
            return redirect("register")
        elif User.objects.filter(username=name).exists():
            messages.error(request,"username already exits")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.error(request,"email taken")
            return redirect("register")
        else:
            u=User.objects.create_user(username=name,email=email,password=p1)
            u.save()
            um=User.objects.get(username=name)
            addprofile=profile.objects.create(fname=fname,lname=lname,uname=name,email=email,address=address,pp=pp)
            print(fname,lname,name,email,address,pp)
            addprofile.save()
            return redirect("logp")
    return render(request,"signup.html")

def logp(request):
    if request.method=="POST":
        un=request.POST.get("un")
        p=request.POST.get("p")
        user=authenticate(username=un,password=p)
        #print(user,un)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"invalid credentials")
            return redirect("logp")
            
    return render(request,"logp.html")

def logd(request):
    if request.method=="POST":
        un=request.POST.get("un")
        p=request.POST.get("p")
        user=authenticate(username=un,password=p)
        #print(user,un)
        if user is not None and user.is_superuser:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"invalid credentials")
            return redirect("logd")
            
    return render(request,"logd.html")

@login_required(login_url='')
def log_out(request):
    logout(request)
    return redirect('/')

@login_required(login_url='')
def home(request):
    return render(request,'home.html',{'name':request.user.username})

