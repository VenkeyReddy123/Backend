# Generated by Django 5.0.2 on 2024-03-10 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0046_rename_adress_adress_adresss'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='ImageUrl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.image'),
        ),
    ]
