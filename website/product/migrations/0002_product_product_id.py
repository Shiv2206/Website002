# Generated by Django 4.2.7 on 2024-04-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_ID',
            field=models.IntegerField(default=1),
        ),
    ]
