from django.shortcuts import render, redirect
from .models import *


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort')
    print(sorting)

    if sorting == 'name':
        phones = Phone.objects.order_by('name')
    elif sorting == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sorting == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print(slug)
    phone = Phone.objects.filter(slug=slug).first()
    print(phone)
    context = {'phone': phone}

    return render(request, template, context)
