# Generated by Django 3.0.5 on 2020-11-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201115_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prod_desc',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
