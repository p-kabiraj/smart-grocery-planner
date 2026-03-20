from django.shortcuts import render
from .models import Product, Price


def home(request):
    return render(request, 'index.html')


def search(request):
    query = request.GET.get('q', '').strip()
    prices = []

    if query:
        # Search for products case-insensitive
        prices = Price.objects.filter(
            product__name__icontains=query
        ).select_related('product', 'platform').order_by('price')

    return render(request, 'index.html', {
        'prices': prices,
        'query': query
    })