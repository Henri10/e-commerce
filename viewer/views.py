from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from .models import Smartphone


def index(request):
    return render(request, template_name="base.html")


def products(request):
    phones = Smartphone.objects.all()
    return render(request, template_name="products.html", context={"phones": phones})


def smartphone(request):
    phones = Smartphone.objects.all()
    all_phones = []
    for phone in phones:
        if phone.products.name == "Smartphone":
            all_phones.append(phone)
    return render(request, template_name="smartphone.html", context={"phones": all_phones})


class Product_details(DetailView):
    template_name = "products_details.html"
    model = Smartphone


def smartwatch(request):
    smartwatches = Smartphone.objects.all()
    all_watch = []
    for watch in smartwatches:
        if watch.products.name == "SmartWatch":
            all_watch.append(watch)
    return render(request, template_name="smartwatch.html", context={"watches": all_watch})
