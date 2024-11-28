from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView


# Create your views here.




class Reservation(View):
    def get(self, request):
        return render(request, 'reservations/reservation.html')