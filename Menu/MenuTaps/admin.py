from django.contrib import admin
from .models import Category, SubCategory


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_display_links = ('category_name',)
    # am ordering  date joined by descending order
    ordering = ('-created_at',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'category_name',)


admin.site.register(SubCategoryAdmin, Category, SubCategory, SubCategoryAdmin)
