# Generated by Django 4.2.7 on 2024-04-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('C_Pass', models.CharField(max_length=100)),
            ],
        ),
    ]
