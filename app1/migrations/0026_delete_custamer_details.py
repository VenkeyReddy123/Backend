# Generated by Django 5.0.2 on 2024-02-21 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_alter_add_to_card_custamer_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Custamer_Details',
        ),
    ]