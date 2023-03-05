from django.contrib import admin
from .models import Category, SubCategory


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_display_links = ('category_name',)
    # am ordering  date joined by descending order
    ordering = ('-created_at',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_name',)


admin.site.register(Category, CategoryAdmin )
admin.site.register(SubCategory, SubCategoryAdmin)
