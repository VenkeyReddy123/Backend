# Generated by Django 5.0.2 on 2024-02-14 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custamer_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_Amount', models.IntegerField()),
                ('City', models.CharField(max_length=100)),
                ('Adress', models.TextField()),
                ('Full_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Custamer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
                ('Order_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.orders')),
            ],
        ),
    ]
