import csv
from saleor.product.models import Category, Product, ProductClass, ProductVariant, ProductAttribute,\
    StockLocation, Stock
from saleor.userprofile.models import Address, User
from saleor.shipping.models import ShippingMethod, ShippingMethodCountry
from saleor.order.models import Order, DeliveryGroup, OrderedItem, OrderHistoryEntry, Payment
from django.contrib.sessions.models import Session
from django.db import connection


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
    with open('/Users/kuliza/export_latest/userprofile_address.csv') as csvfile:
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
    with open('/Users/kuliza/export_latest/userprofile_user.csv') as csvfile:
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


def populate_userprofile_user_addresses():
    with open('/Users/kuliza/export_latest/userprofile_user_addresses.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_id = row['user_id']
            address_id = row['address_id']
            user = User.objects.get(id=user_id)
            address = Address.objects.get(id=address_id)
            user.addresses.add(address)
            user.save()


def populate_shipping_shippingmethod():
    with open('/Users/kuliza/export_latest/shipping_shippingmethod.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            xid = row['id']
            name = row['name']
            description = row['description']
            ShippingMethod.objects.create(id=xid, name=name, description=description)


def populate_shipping_shippingmethodcountry():
    with open('/Users/kuliza/export_latest/shipping_shippingmethodcountry.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            xid = row['id']
            country_code = row['country_code']
            shipping_method_id = row['shipping_method_id']
            price = row['price']
            ShippingMethodCountry.objects.create(id=xid, country_code=country_code,
                                                 shipping_method_id=shipping_method_id, price=price)


def populate_django_sessions():
    with open('/Users/kuliza/export_latest/django_session.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            session_key = row['session_key']
            session_data = row['session_data']
            expire_date = row['expire_date']
            Session.objects.create(session_key=session_key, session_data=session_data, expire_date=expire_date)


def populate_order_order():
    with open('/Users/kuliza/export_latest/order_order.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            xid = row['id']
            status = row['status']
            created = row['created']
            tracking_client_id = row['tracking_client_id']
            user_email = row['anonymous_user_email']
            billing_address_id = row['billing_address_id']
            shipping_address_id = row['shipping_address_id']
            user_id = row['user_id']
            total_net = row['total_net']
            total_tax = row['total_tax']
            Order.objects.create(id=xid, status=status, created=created, tracking_client_id=tracking_client_id,
                                 user_email=user_email, billing_address_id=billing_address_id, shipping_address_id=shipping_address_id,
                                 user_id=user_id, total_net=total_net, total_tax=total_tax)


def populate_order_deliverygroup():
    with open('/Users/kuliza/export_latest/order_deliverygroup.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            xid = row['id']
            status = row['status']
            order_id = row['order_id']
            last_updated = row['last_updated']
            tracking_number = row['tracking_number']
            shipping_method_name = row['shipping_method_name']
            shipping_price = row['shipping_price']

            DeliveryGroup.objects.create(id=xid, status=status, order_id=order_id, last_updated=last_updated,
                                         tracking_number=tracking_number, shipping_method_name=shipping_method_name,
                                         shipping_price=shipping_price)


def populate_order_ordereditem():
    with open('/Users/kuliza/export_latest/order_ordereditem.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            xid = row['id']
            product_name = row['product_name']
            product_sku = row['product_sku']
            quantity = row['quantity']
            unit_price_net = row['unit_price_net']
            unit_price_gross = row['unit_price_gross']
            delivery_group_id = row['delivery_group_id']
            product_id = row['product_id']
            stock_id = row['stock_id']
            stock_location = row['stock_location']

            OrderedItem.objects.create(id=xid, product_name=product_name, product_sku=product_sku, quantity=quantity,
                                       unit_price_net=unit_price_net, unit_price_gross=unit_price_gross,
                                       delivery_group_id=delivery_group_id, product_id=product_id, stock_id=stock_id,
                                       stock_location=stock_location)


def populate_order_orderhistoryentry():
    with open('/Users/kuliza/export_latest/order_orderhistoryentry.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            xid = row['id']
            date = row['date']
            status = row['status']
            comment = row['comment']
            order_id = row['order_id']
            user_id = row['user_id']

            OrderHistoryEntry.objects.create(id=xid, date=date, status=status, comment=comment, order_id=order_id,
                                             user_id=user_id)


def populate_order_payment():
    with open('/Users/kuliza/export_latest/order_payment.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            xid = row['id']
            variant = row['variant']
            fraud_status = row['fraud_status']
            fraud_message = row['fraud_message']
            created = row['created']
            modified = row['modified']
            transaction_id = row['transaction_id']
            currency = row['currency']
            total = row['total']
            delivery = row['delivery']
            tax = row['tax']
            description = row['description']
            billing_first_name = row['billing_first_name']
            billing_last_name = row['billing_last_name']
            billing_address_1 = row['billing_address_1']
            billing_address_2 = row['billing_address_2']
            billing_city = row['billing_city']
            billing_postcode = row['billing_postcode']
            billing_country_code = row['billing_country_code']
            billing_country_area = row['billing_country_area']
            billing_email = row['billing_email']
            extra_data = row['extra_data']
            message = row['message']
            token = row['token']
            captured_amount = row['captured_amount']
            order_id = row['order_id']
            customer_ip_address = row['customer_ip_address']
            Payment.objects.create(id=xid, variant=variant, fraud_status=fraud_status, fraud_message=fraud_message,
                                   created=created, modified=modified, transaction_id=transaction_id, currency=currency,
                                   total=total, delivery=delivery, tax=tax, description=description,
                                   billing_first_name=billing_first_name, billing_last_name=billing_last_name,
                                   billing_address_1=billing_address_1, billing_address_2=billing_address_2,
                                   billing_city=billing_city, billing_postcode=billing_postcode,
                                   billing_country_code=billing_country_code, billing_country_area=billing_country_area,
                                   billing_email=billing_email, extra_data=extra_data, message=message, token=token,
                                   captured_amount=captured_amount, order_id=order_id,
                                   customer_ip_address=customer_ip_address)


def set_sequence():
    sequences = ['account_emailaddress_id_seq', 'account_emailconfirmation_id_seq', 'auth_group_id_seq',
                 'auth_group_permissions_id_seq', 'auth_permission_id_seq', 'cart_cartline_id_seq',
                 'discount_sale_categories_id_seq', 'discount_sale_id_seq', 'discount_sale_products_id_seq',
                 'discount_voucher_id_seq', 'django_admin_log_id_seq', 'django_content_type_id_seq',
                 'django_prices_openexchangerates_conversionrate_id_seq', 'django_site_id_seq',
                 'order_deliverygroup_id_seq', 'order_order_id_seq', 'order_ordereditem_id_seq',
                 'order_orderhistoryentry_id_seq', 'order_ordernote_id_seq', 'order_payment_id_seq',
                 'product_attributechoicevalue_id_seq', 'product_category_id_seq', 'product_product_categories_id_seq',
                 'product_product_id_seq', 'product_productattribute_id_seq', 'product_productclass_id_seq',
                 'product_productclass_product_attributes_id_seq', 'product_productclass_variant_attributes_id_seq',
                 'product_productimage_id_seq', 'product_productvariant_id_seq', 'product_stock_id_seq',
                 'product_stocklocation_id_seq', 'product_variantimage_id_seq', 'shipping_shippingmethod_id_seq',
                 'shipping_shippingmethodcountry_id_seq', 'site_sitesettings_id_seq', 'userprofile_address_id_seq',
                 'userprofile_user_addresses_id_seq', 'userprofile_user_groups_id_seq', 'userprofile_user_id_seq',
                 'userprofile_user_user_permissions_id_seq']

    with connection.cursor() as cursor:
        for seq in sequences:
            sequence_table = seq.replace('_id_seq', '')
            cursor.execute("SELECT setval('%s', max(id)) FROM %s;" % (seq, sequence_table))
            row = cursor.fetchone()
            print row


#truncate table userprofile_address CASCADE;
def populate():
    # popupate_categories()
    # populate_products()
    # populate_product_product_category()
    # populate_product_productattribute()
    # populate_product_productvariant()
    # populate_product_stock()

    # populate_userprofile_address()
    # populate_userprofile_user()
    # populate_userprofile_user_addresses()
    # populate_shipping_shippingmethod()
    # populate_shipping_shippingmethodcountry()
    # populate_django_sessions()
    # populate_order_order()
    # populate_order_deliverygroup()
    # populate_order_ordereditem()
    # populate_order_orderhistoryentry()
    # populate_order_payment()

    set_sequence()
