# Generated by Django 2.2 on 2019-09-18 15:00

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190917_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, upload_to=products.models.upload_image_path),
        ),
    ]
