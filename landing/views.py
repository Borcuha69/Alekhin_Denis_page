from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(requests):
    return render(requests, 'landing/landing.html', locals())


def t_shop(requests):
    products = ProductImage.objects.filter(is_active= True, is_main= True)
    products_phone = products.filter(product__category_id=1)
    products_laptop = products.filter(product__category_id=2)
    return render(requests, 'landing/T-Shop.html', locals())