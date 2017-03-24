import csv
from saleor.product.models import Category, Product


def popupate_categories():
    with open('/Users/kuliza/product_category.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cat_id = row['id']
            name = row['name']
            slug = row['slug']
            hidden = row['hidden']
            parent_id = row['parent_id']
            tree_id = row['tree_id']
            lft = row['lft']
            rght = row['rght']
            level = row['level']
            Category.objects.create(id=cat_id, name=name, slug=slug, hidden=hidden, parent_id=parent_id,
                                    tree_id=tree_id, lft=lft, rght=rght, level=level)


def populate_products():
    with open('/Users/kuliza/product_product.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            prod_id = row['id']
            name = row['name']
            description = row['description']
            price = row['price']
            available_on = row['available_on']
            updated_at = row['updated_at']
            Product.objects.create(id=prod_id, name=name, description=description, price=price,
                                   available_on=available_on, updated_at=updated_at, product_class_id=1)


if __name__ == '__main__':
    populate_products()
