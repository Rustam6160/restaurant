
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView


# Create your views here.


class Menu(View):
    def get(self, request):
        dishes = Dish.objects.all()
        categories = Category.objects.all()

        return render(request, "menu/menu.html", context={'dishes': dishes, 'categories': categories})


