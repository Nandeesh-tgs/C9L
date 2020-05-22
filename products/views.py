from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from .models import Products
from .models import Supplier
from .choices import Passenger_choices, state_choices, stops_choices


def index(request):
    products = Products.objects.all()

    paginator =Paginator(products,6)
    page=request.GET.get('page')
    paged_products=paginator.get_page(page)

    context = {
        'products': paged_products,
       
    }

    return render(request, 'products/products.html', context )


def product(request, product_id):

    product=get_object_or_404(Products, pk=product_id)

    context= {
        'product': product
    }

    return render(request, 'products/product.html', context)

def search(request):
    queryset_listp =Products.objects.order_by('-list_date')
    queryset_lists =Supplier.objects.order_by('-list_date')

#keywords both supplier and products
    if 'keywords' in request.GET:
       keywords = request.GET['keywords']
       if keywords:
           queryset_listp = queryset_listp.filter(description__icontains=keywords)
           queryset_lists = queryset_lists.filter(about_company__icontains=keywords)

#city with supplier list
    if 'city' in request.GET:
       city = request.GET['city']
       if city:
           queryset_lists = queryset_lists.filter(city__iexact=city)
#State with supplier list
    if 'state' in request.GET:
       state = request.GET['state']
       if state:
           queryset_lists = queryset_lists.filter(state__iexact=state)
#passenger with products list
    if 'Passenger' in request.GET:
       passenger = request.GET['Passenger']
       if Passenger:
           queryset_listp = queryset_listp.filter(Passenger__lte=passenger)
#stops with products list
    if 'stops' in request.GET:
       stops = request.GET['stops']
       if stops:
           queryset_listp = queryset_listp.filter(Num_stops__lte=stops)


    context = {
        'Passenger_choices': Passenger_choices,
        'stops_choices':stops_choices,
        'state_choices':state_choices,
        'Products':queryset_listp,
        'Supplier':queryset_lists,
        'values': request.GET

    }

    return render(request, 'products/search.html', context)


