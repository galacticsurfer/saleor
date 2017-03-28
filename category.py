import csv
from saleor.product.models import Category, Product, ProductClass, ProductVariant, ProductAttribute,\
    StockLocation, Stock
from saleor.userprofile.models import Address, User


def popupate_categories():
    with open('/Users/kuliza/export/product_category.csv') as csvfile:
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
    with open('/Users/kuliza/export/product_product.csv') as csvfile:
        ProductClass.objects.create()
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


def populate_product_product_category():
    with open('/Users/kuliza/export/product_product_categories.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product_id = row['product_id']
            category_id = row['category_id']

            product = Product.objects.get(id=product_id)
            category = Category.objects.get(id=category_id)

            if category.id not in [1, 5, 9, 20, 62, 64]:
                product.categories.add(category)
                product.save()


def populate_product_productvariant():
    with open('/Users/kuliza/export/product_productvariant.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pid = row['id']
            sku = row['sku']
            name = row['name']
            product_id = row['product_id']

            ProductVariant.objects.create(id=pid, sku=sku, name=name, attributes={}, product_id=product_id)


def populate_product_productattribute():
    with open('/Users/kuliza/export/product_productattribute.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pid = row['id']
            name = row['name']
            display = row['display']
            ProductAttribute.objects.create(id=pid, name=name, display=display)


def populate_product_stock():
    with open('/Users/kuliza/export/product_stock.csv') as csvfile:
        StockLocation.objects.create(name="Bangalore")
        reader = csv.DictReader(csvfile)
        for row in reader:
            pid = row['id']
            location = 1
            quantity = row['quantity']
            quantity_allocated = row['quantity_allocated']
            variant_id = row['variant_id']
            Stock.objects.create(id=pid, location_id=location, quantity=quantity, quantity_allocated=quantity_allocated,
                                 variant_id=variant_id)


def populate_userprofile_address():
    with open('/Users/kuliza/export/userprofile_address.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            address_id = row['id']
            first_name = row['first_name']
            last_name = row['last_name']
            company_name = row['company_name']
            street_address_2 = row['street_address_2']
            city = row['city']
            postal_code = row['postal_code']
            country = row['country']
            country_area = row['country_area']
            phone = row['phone']
            city_area = row['city_area']
            street_address_1 = row['street_address_1']

            Address.objects.create(id=address_id, first_name=first_name, last_name=last_name, company_name=company_name,
                                   street_address_2=street_address_2, city=city, postal_code=postal_code,
                                   country=country, country_area=country_area, phone=phone, city_area=city_area,
                                   street_address_1=street_address_1)


def populate_userprofile_user():
    with open('/Users/kuliza/export/userprofile_user.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_id = row['id']
            is_superuser = row['is_superuser']
            email = row['email']
            is_staff = row['is_staff']
            password = row['password']
            date_joined = row['date_joined']
            last_login = row['last_login']
            default_billing_address_id = row['default_billing_address_id']
            default_shipping_address_id = row['default_shipping_address_id']

            User.objects.create(id=user_id, is_superuser=is_superuser, email=email, is_staff=is_staff,
                                password=password, date_joined=date_joined, last_login=last_login,
                                default_billing_address_id=default_billing_address_id,
                                default_shipping_address_id=default_shipping_address_id)


def populate():
    popupate_categories()
    populate_products()
    populate_product_product_category()
    populate_product_productattribute()
    populate_product_productvariant()
    populate_product_stock()
    populate_userprofile_address()
    populate_userprofile_user()
