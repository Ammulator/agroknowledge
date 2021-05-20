from django.urls import path

from . import views

urlpatterns = [

    path('',views.contacts,name='contacts'),
    path('contactsubmit',views.contactsubmit,name='contactsubmit'),
]
