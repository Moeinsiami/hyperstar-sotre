from django.shortcuts import render

from store.models import Product


def index(request):
    products = Product.objects.all()
    newest_products = Product.objects.order_by('-created')[:10]
    context = {
        'products': products,
        'newest_products': newest_products
    }
    return render(request, 'index.html', context)


def contact_us(request):
    return render(request, 'contact-us.html')