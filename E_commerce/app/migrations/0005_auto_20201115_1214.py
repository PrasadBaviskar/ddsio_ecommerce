# Generated by Django 3.0.5 on 2020-11-15 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201114_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='cat_img',
            field=models.ImageField(blank=True, null=True, upload_to='categories'),
        ),
        migrations.AlterField(
            model_name='products',
            name='prod_img',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
