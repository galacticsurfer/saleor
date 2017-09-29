from django.core.management import BaseCommand

from saleor.search import elastic_search
from saleor.product import models as project_models
from saleor.product import search_indexes as product_indexes


class Command(BaseCommand):
    help = 'For re-building indexes'

    def handle(self, *args, **options):
        """
        to re-build index in elastic search
        :return:
        """
        elastic_search_client = elastic_search.ElasticSearch()
        self.stdout.write('Rebuilding product indexes.')
        elastic_search_client.rebuild_index(index_class=product_indexes.ProductIndex,
                                            model=project_models.Product, index_name='product')
        self.stdout.write('Product indexes rebuilding successful.')

