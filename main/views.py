from django.shortcuts import render
from . import models

def index(request):
    banner = models.Banner.objects.last()
    about_us = models.About_us.objects.last()
    services = models.Service.objects.all()
    footer = models.Footer.objects.last()

    prices_list = []

    for price in models.Price.objects.all().order_by('price'):
        price.body = price.body.split(',')
        prices_list.append(price)
    
    context = {
        'banner':banner,
        'about_us':about_us,
        'services':services,
        'prices':prices_list,
        'footer':footer
    }

    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        # try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                message=request.POST['message'],
                )
        # except:
        #     ...
    return render(request, 'contact.html')


def about(request):
    banner = models.Banner.objects.last()
    abouts = models.About_us.objects.last()
    footer = models.Footer.objects.last()
    context = {
        'banner': banner,
        'about': abouts,
        'footer': footer
    }
    return render(request, 'about.html',context)


def price(request):
    banner = models.Banner.objects.last()
    footer = models.Footer.objects.last()
    prices = []
    for i in models.Price.objects.all():
        i.body = i.body.split(',')
        prices.append(i)

    context = {
        'banner':banner,
        'prices':prices,
        'footer':footer
    }
    return render(request, 'price.html',context)


def service(request):
    banner = models.Banner.objects.last()
    services = models.Service.objects.all()
    footer = models.Footer.objects.last()

    context = {
        'banner':banner,
        'services':services,
        'footer':footer,
    }

    return render(request, 'service.html', context)
