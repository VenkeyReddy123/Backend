# Generated by Django 5.0.2 on 2024-02-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_custamer_details_custamer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_Pic',
            field=models.ImageField(upload_to=''),
        ),
    ]