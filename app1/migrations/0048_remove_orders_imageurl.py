# Generated by Django 5.0.2 on 2024-03-10 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0047_orders_imageurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='ImageUrl',
        ),
    ]
