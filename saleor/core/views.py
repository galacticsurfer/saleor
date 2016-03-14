from django.template.response import TemplateResponse

from ..product.models import Product
from .utils import get_paginator_items
from django.conf import settings


def home(request):
    products = Product.objects.get_available_products()
    products = products.prefetch_related('categories', 'images',
                                         'variants__stock')
    products = get_paginator_items(
        products, settings.PAGINATE_BY, request.GET.get('page'))
    return TemplateResponse(
        request, 'base.html',
        {'products': products, 'parent': None})
