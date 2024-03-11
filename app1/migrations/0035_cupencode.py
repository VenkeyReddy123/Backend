# Generated by Django 5.0.2 on 2024-02-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0034_delete_cupencode'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupenCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code_Name', models.CharField(max_length=10)),
                ('Discount_Type', models.CharField(max_length=20)),
                ('Code_Off', models.IntegerField()),
                ('ExpireDate', models.DateTimeField()),
                ('HowMany_Days', models.IntegerField()),
                ('Limit', models.IntegerField()),
            ],
        ),
    ]
