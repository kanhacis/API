# Generated by Django 5.0.3 on 2024-04-02 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0027_mystore_location_mystore_status_mystore_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_images', to='mystore.storeitem'),
        ),
    ]
