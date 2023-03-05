from django.shortcuts import render
from.models import Product,SubCategory,Category
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home_page(request, category_slug=None):
    categories = None
    product = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=categories, published=True) & Listing.objects.filter(
            category=categories, rented=false)
        listings_count = Listing.count()
    else:
        listings = Listing.objects.all().filter(published=True).order_by('created_at') & Listing.objects.all().filter(
            rented=False)
        listings_count = Listing.objects.all().count()
    context = {
        'listings': listings,
        'listings_count': listings_count,
    }
    return render(request, "home/yindex.html", context)
