from unicodedata import category

from django.db import models
from django.urls import reverse


def my_slugify(text):
    idn = random.randint(1, 50000)
    text = text.lower()
    unsafe = [letter for letter in text if letter == " "]
    if unsafe:
        for letter in unsafe:
            text = text.replace(letter, '-')
    text = u'_'.join(text.split())
    text = f'{text}-{idn}'
    return text
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.slug = my_slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])


class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.subcategory_name

    def save(self, *args, **kwargs):
        self.slug = my_slugify(self.subcategory_name)
        super(SubCategory, self).save(*args, **kwargs)


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.slug = my_slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

