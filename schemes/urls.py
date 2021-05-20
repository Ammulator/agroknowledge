from django.urls import path

from . import views

urlpatterns = [
    
    path('services',views.schemes,name='services'),

]