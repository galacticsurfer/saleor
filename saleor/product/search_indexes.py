from elasticsearch_dsl import DocType, Integer, String, Float
from saleor.product.models import ProductImage


class ProductIndex(DocType):
    """
    Index for product model
    """
    id = Integer()
    name = String()
    price = Float()
    category = String()
    image_url = String()
    hidden = Integer()

    class Meta:
        index = 'product'

    @classmethod
    def from_obj(cls, obj):
        try:
            product_image = ProductImage.objects.get(product_id=obj.id)
        except ProductImage.DoesNotExist:
            product_image = None
        except ProductImage.MultipleObjectsReturned:
            product_image = ProductImage.objects.filter(product_id=obj.id).first()

        if product_image:
            image_name = product_image.image.url.split('/')[-1]
            ix = image_name.split('.')
            ext = ix[-1]
            px = '.'.join(ix[0:len(ix)-1])
            if ext.lower() == 'png':
                image_url = "/media/__sized__/products/%s-crop-c0-5__0-5-100x100.%s" % (px, ext)
            else:
                image_url = "/media/__sized__/products/%s-crop-c0-5__0-5-100x100-70.%s" % (px, ext)
        else:
            image_url = ''

        category = obj.categories.first()

        if category.hidden:
            hidden = 1
        else:
            hidden = 0

        category_name = obj.categories.first().name

        return cls(id=obj.id, name=obj.name, price=obj.price[0], category=category_name, image_url=image_url,
                   hidden=hidden)

