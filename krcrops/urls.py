from django.urls import path
from . import views

urlpatterns = [
    
    #Rabi
    path('wheat',views.wheat,name='wheat'),
    path('gram',views.gram,name='gram'),
    path('sunflower',views.sunflower,name='sunflower'),
    path('potato',views.potato,name='potato'),
    path('onion',views.onion,name='onion'),
    path('tomato',views.tomato,name='tomato'),
    
    #Kharif
    path('rice',views.rice,name='rice'),
    path('corn',views.corn,name='corn'),
    path('soyabean',views.soyabean,name='soyabean'),
    path('cotton',views.cotton,name='cotton'),
    path('sugarcane',views.sugarcane,name='sugarcane'),
    path('moong',views.moong,name='moong'),

]