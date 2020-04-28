from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from random import random
import math
import uuid
import os
from django.utils._os import safe_join


class ProductManager(models.Manager):
    def created_by_cat_id(self, name, cat_id):
        cat = Category.objects.get(id=cat_id)
        price = math.floor(random()*200)
        quantity = math.floor(random()*40)
        return Product.objects.create(category=cat, name=name, price=price, quantity_avialable=quantity, featured=True)

    def all(self, *args, **kwargs):
        return Product.objects.filter(quantity_avialable__gte=1, featured=True)


def path_and_rename(prefix, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return (os.path.join(prefix, filename))


def get_path_for_my_model_file(instance, filename):
    return path_and_rename('product_image/', filename)


class Product(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name="product")
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(default=None, blank=True, null=True)
    # photo = models.FileField(upload_to='product_image',default=None, blank=True)
    photo = models.ImageField(
        upload_to=get_path_for_my_model_file, default=None, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity_avialable = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return '{id} - {name} - {price}$ --- {quantity}'.format(id=self.id, name=self.name, price=self.price, quantity=self.quantity_avialable)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def is_featured(self):
        return self.featured


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# def category_pre_saved_receiver(sender, instance, created, *args, **kwargs):
# 	category = instance
# 	variations = category.variation_set.all()
# 	if not category.slug:
# 		new_var = Category()
# 		new_var.name = category.name
# 		new_var.slug = slugify(category.name)
# 		new_var.description = category.description
# 		new_var.active = category.active
# 		new_var.save()


# pre_save.connect(category_pre_saved_receiver, sender=Category)
