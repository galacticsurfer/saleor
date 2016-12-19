from django.template.response import TemplateResponse

from ..product.models import Product
from .utils import get_paginator_items
from django.conf import settings


class Message(object):
    def __init__(self, m):
        self.message = m
        self.tags = 'danger'

    def __str__(self):
        return self.message

message = Message('Orders placed after 20th Dec 2016 will be processed after 3rd Jan 2017, Merry Christmas and a '
                  'Happy New Year to all !')


def home(request):
    products = Product.objects.get_available_products().order_by('-counter')
    products = products.prefetch_related('categories', 'images',
                                         'variants__stock')
    products = get_paginator_items(
        products, settings.PAGINATE_BY, request.GET.get('page'))
    return TemplateResponse(
        request, 'base.html',
        {'products': products, 'parent': None, 'show_banner': True, 'messages': [message]})
