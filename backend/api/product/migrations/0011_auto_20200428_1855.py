# Generated by Django 2.2 on 2020-04-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200428_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default=None, upload_to='product_image'),
        ),
    ]