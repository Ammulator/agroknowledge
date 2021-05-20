from django.urls import path
from . import views

urlpatterns = [
    
    #rabi
    path('',views.wheatmsp,name='wheatmsp'),
    path('grammsp',views.grammsp,name='grammsp'),
    path('sunflowermsp',views.sunflowermsp,name='sunflowermsp'),
    path('potatomsp',views.potatomsp,name='potatomsp'),
    path('onionmsp',views.onionmsp,name='onionmsp'),
    path('tomatomsp',views.tomatomsp,name='tomatomsp'),

    #Kharif
    path('ricemsp',views.ricemsp,name='ricemsp'),
    path('cornmsp',views.cornmsp,name='cornmsp'),
    path('soyabeanmsp',views.soyabeanmsp,name='soyabeanmsp'),
    path('cottonmsp',views.cottonmsp,name='cottonmsp'),
    path('sugarcanemsp',views.sugarcanemsp,name='sugarcanemsp'),
    path('moongmsp',views.moongmsp,name='moongmsp'),

]