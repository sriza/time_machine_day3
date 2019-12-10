from django.contrib import admin
from django.urls import path
from time_teller.views import home,today,times

urlpatterns = [
    path('',home),
    path('today/',today),
    path('timestamp/',times)

]
