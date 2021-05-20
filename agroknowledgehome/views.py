from django.shortcuts import render
from .models import news
# Create your views here.
def index(request):

    new=news.objects.all()

    return render(request,'index.html',{'new':new})