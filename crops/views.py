from django.shortcuts import render
from .models import rcrops, kcrops
# Create your views here.
def crops(request):
   

    rabi=rcrops.objects.all()

    kharif=kcrops.objects.all()


    

    return render(request,'products.html',{'crops':rabi,'kharif':kharif})
