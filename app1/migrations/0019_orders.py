# Generated by Django 5.0.2 on 2024-02-14 16:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_remove_orders_product_name_remove_orders_username_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('Order_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Delivary_Type', models.CharField(max_length=100)),
                ('Payment_Status', models.CharField(max_length=100)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Custamer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
                ('Product_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.products')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
