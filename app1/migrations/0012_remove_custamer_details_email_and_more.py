# Generated by Django 5.0.2 on 2024-02-14 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_orders_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custamer_details',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='custamer_details',
            name='Order_Id',
        ),
        migrations.RemoveField(
            model_name='custamer_details',
            name='username',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='Custamer_Name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='Custamer_Name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='Product_Name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='username',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='Product_Name',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='Add_TO_Card',
        ),
        migrations.DeleteModel(
            name='Custamer_Details',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
