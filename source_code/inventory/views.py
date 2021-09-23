from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def check_inv(request):
    prod=Products.objects.all()
    return render(request, "view_inv.html", {'prods':prod})

def home(request):
    return render(request, "inventory.html")

def add_inv(request):
    return render(request, "add_inv.html")

def add_prod(request):
    pname= request.POST['name']
    pprod_price= request.POST['prod_price']
    pquantity= int(request.POST['quantity'])
    if len(Products.objects.filter(name=pname))==1:
        a=Products.objects.get(name=pname)
        a.quantity = a.quantity + pquantity
        Products.objects.filter(name=pname).update(price=pprod_price, quantity=a.quantity)
        p=Products.objects.all()
        return render(request, "view_inv.html", {'prods':p})
    else:
        Products.objects.create(name=pname, price=pprod_price, quantity=pquantity)
        q=Products.objects.all()
        return render(request, "view_inv.html", {'prods':q})

def rem_inv(request):
    return render(request, "remove_inv.html")

def rem_prod(request):
    pname=request.POST['name']
    pquantity= int(request.POST['quantity'])
    b=Products.objects.get(name=pname)
    if b.quantity==0:
        return render(request, "rem_inv2.html")
    elif len(Products.objects.filter(name=pname))==1:
        b.quantity = b.quantity-pquantity
        if (b.quantity)<0:
            return render(request, "rem_inv4.html")
        Products.objects.filter(name=pname).update(quantity=b.quantity)
        p=Products.objects.all()
        return render(request, "view_inv.html", {'prods':p})
    else:
        return render(request, "rem_inv3.html")