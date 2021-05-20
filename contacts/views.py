from django.shortcuts import render
from datetime import datetime
from contacts.models import Contact

def contacts(request):
    return render(request,"contacts.html")


def contactsubmit(request):   

    if request.method=="POST":

        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]

        c=Contact(name=name,email=email,phone_no=phone,desc=message)
        c.save()

    return render(request,"contacts.html")