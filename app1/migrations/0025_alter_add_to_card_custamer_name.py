# Generated by Django 5.0.2 on 2024-02-19 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_add_to_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_to_card',
            name='Custamer_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.login'),
        ),
    ]