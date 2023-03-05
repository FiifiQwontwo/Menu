from django.urls import path
from .views import *

app_name = 'MenuTaps'

urlpatterns = [
    path('', home_page, name='home_page_urls'),
    # path('<slug:category_slug>/', home_page, name='product_by_category'),


]
