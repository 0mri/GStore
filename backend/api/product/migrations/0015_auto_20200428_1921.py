# Generated by Django 2.2 on 2020-04-28 16:21

import backend.api.product.models
from django.db import migrations, models
import storages.backends.dropbox


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20200428_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default=None, storage=storages.backends.dropbox.DropBoxStorage(), upload_to=backend.api.product.models.get_path_for_my_model_file),
        ),
    ]
