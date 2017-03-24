# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0004_auto_20170206_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='type',
            field=models.CharField(choices=[('fixed', 'INR'), ('percentage', '%')], default='fixed', max_length=10, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='discount_value_type',
            field=models.CharField(choices=[('fixed', 'INR'), ('percentage', '%')], default='fixed', max_length=10, verbose_name='discount type'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='limit',
            field=django_prices.models.PriceField(blank=True, currency='INR', decimal_places=2, max_digits=12, null=True, verbose_name='limit'),
        ),
    ]
