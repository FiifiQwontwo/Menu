from .models import Category,SubCategory


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def submenu_links(request):
    links = SubCategory.objects.all()