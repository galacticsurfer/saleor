from django.template.response import TemplateResponse

from ..product.utils import products_with_availability, products_for_homepage

class Message(object):
    def __init__(self, m):
        self.message = m
        self.tags = 'warning'

    def __str__(self):
        return self.message

message = Message('Please note that, Orders placed on or after 21/08/2017 will be processed only after 28/08/2017.')

def home(request):
    products = products_for_homepage()[:8]
    products = products_with_availability(
        products, discounts=request.discounts, local_currency=request.currency)
    return TemplateResponse(
        request, 'home.html',
        {'products': products, 'parent': None})
