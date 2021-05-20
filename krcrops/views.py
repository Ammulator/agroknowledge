from django.shortcuts import render

# Create your views here.

#Rabi
def wheat(request):

    return render(request,'wheat.html')

def gram(request):

    return render(request,'gram.html')

def sunflower(request):

    return render(request,'sunflower.html')

def potato(request):

    return render(request,'potato.html')

def onion(request):

    return render(request,'onion.html')

def tomato(request):

    return render(request,'tomato.html')

#Kharif

def rice(request):

    return render(request,'rice.html')

def corn(request):

    return render(request,'corn.html')

def soyabean(request):

    return render(request,'soyabean.html')

def cotton(request):

    return render(request,'cotton.html')

def sugarcane(request):

    return render(request,'sugarcane.html')

def moong(request):

    return render(request,'moong.html')
