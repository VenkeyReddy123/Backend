# Generated by Django 5.0.2 on 2024-03-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0041_checkcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='ImageUrl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
