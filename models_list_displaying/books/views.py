from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from datetime import datetime


def books(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    catalog = Book.objects.all()
    context = {'books': catalog}
    return render(request, template, context)


def data_view(request, data):
    template = 'books/book_date.html'
    # sort_data = request.GET.get(data)
    # print(sort_data)
    catalog = Book.objects.filter(pub_date=data)

    next_date = Book.objects.filter(pub_date__gt=data).values_list('pub_date').order_by('pub_date').first()
    if next_date:
        next_date = next_date[0].strftime("%Y-%m-%d")

    prev_date = Book.objects.filter(pub_date__lt=data).values_list('pub_date').order_by('-pub_date').first()
    if prev_date:
        prev_date = prev_date[0].strftime("%Y-%m-%d")

    context = {
        'books': catalog,
        'b_prev': prev_date,
        'b_next': next_date
    }

    # page = int(request.GET.get('page', 1))
    # elements_per_page = 10
    # paginator = Paginator(catalog, elements_per_page)
    # page_ = paginator.get_page(page)
    # content = page_.object_list
    #
    # context = {
    #     'bus_stations': content,
    #     'page': page_,
    # }
    return render(request, template, context)
