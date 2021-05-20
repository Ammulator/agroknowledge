from django.urls import path

from . import views

urlpatterns = [

    path('products',views.crops,name='products'),
]