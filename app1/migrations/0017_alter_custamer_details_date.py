# Generated by Django 5.0.2 on 2024-02-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_orders_custamer_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custamer_details',
            name='Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
