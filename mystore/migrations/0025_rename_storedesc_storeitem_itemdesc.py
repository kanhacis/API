# Generated by Django 4.0.3 on 2024-03-28 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0024_rename_description_storeitem_storedesc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storeitem',
            old_name='storeDesc',
            new_name='itemDesc',
        ),
    ]
