# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-18 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20180818_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='img',
            field=models.CharField(default='https://www.google.co.in/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi8u_Gj_fbcAhWKpo8KHTXeBvYQjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFile%3ARBS_logo.svg&psig=AOvVaw0RYDi2wAr9EkbDY3QhjNrg&ust=1534694661442463', max_length=100000000000000000),
        ),
    ]
