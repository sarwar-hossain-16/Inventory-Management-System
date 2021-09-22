from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

# Create your views here.
def login1(request):
    return render(request, "login.html")

def checkpass(request):
    val_user= request.POST['username']
    val_pass= request.POST['password']
    x=Users.objects.filter(userid=val_user)
    if len(x)==0:
        return render(request, "login2.html");
    a=Users.objects.get(userid=val_user)
    if(a.passw==val_pass):
        return render(request, "inventory.html");
    else:
        return render(request, "login2.html");