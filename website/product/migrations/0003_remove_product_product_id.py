# Generated by Django 4.2.7 on 2024-04-25 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_ID',
        ),
    ]
