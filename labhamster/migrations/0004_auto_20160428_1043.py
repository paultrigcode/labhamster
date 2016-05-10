# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labhamster', '0003_auto_20160413_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True, verbose_name=b'Currency Code, e.g. USD')),
                ('name', models.CharField(help_text=b'full name', max_length=30, verbose_name=b'Name')),
                ('symbol', models.CharField(blank=True, help_text=b'paste unicode character, e.g. $', max_length=3, unique=True, verbose_name=b'Symbol')),
                ('is_default', models.BooleanField(default=False, help_text=b'make this the default currency', verbose_name=b'make Default')),
            ],
            options={
                'ordering': ('is_default', 'code'),
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='labhamster.Currency', verbose_name=b''),
        ),
    ]