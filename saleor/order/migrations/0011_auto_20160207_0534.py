# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 11:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ("discount", "0003_auto_20160207_0534"),
        ("order", "0010_auto_20160119_0541"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="discount_amount",
            field=django_prices.models.MoneyField(
                blank=True,
                currency=settings.DEFAULT_CURRENCY,
                decimal_places=2,
                max_digits=12,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="discount_name",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="order",
            name="voucher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="discount.Voucher",
            ),
        ),
    ]
