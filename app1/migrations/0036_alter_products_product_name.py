# Generated by Django 5.0.2 on 2024-02-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0035_cupencode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Product_Name',
            field=models.CharField(max_length=1000),
        ),
    ]