from django.urls import path
from .views import *
urlpatterns = [
    path('Dashboard/',dashboard,name='dashboard'),
    path('addproperty/',addProperty,name='addproperty'),
    path('addtenant/',addTenant,name='addtenant'),
    path('allotproperty/',allotproperty,name = 'allotproperty'),
]
