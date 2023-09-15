from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from .models import Smartphone


def index(request):
    return render(request, template_name="base.html")

def smartphone(request):
    phones = Smartphone.objects.all()
    return render(request, template_name="smartphone.html", context={"phones": phones})

class Smartphone_details(DetailView):
    template_name = "smartphone_details.html"
    model = Smartphone



