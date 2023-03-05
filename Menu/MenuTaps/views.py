from .models import Product, Category
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404

from .models import Product, Category


# Create your views here.
def home_page(request, category_slug=None):
    categories = None
    product = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=categories)
    else:
        product = Product.objects.all().order_by('created_at')

    context = {
        'product': product,

    }
    return render(request, "home/index.html", context)
