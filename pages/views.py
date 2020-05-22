from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products
from suppliers.models import Supplier
from products.choices import Passenger_choices, state_choices, stops_choices



def index(request):
    products= Products.objects.order_by('-product_date')[:3]

    context = {
        'products':products,
        'Passenger_choices': Passenger_choices,
        'stops_choices':stops_choices,
        'state_choices':state_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):

    supplier= Supplier.objects.all()


    mvp_supplier=Supplier.objects.all().filter(is_mvp=True)


    context = {
         'supplier': supplier
     }
   

    return render(request, 'pages/about.html', context)
