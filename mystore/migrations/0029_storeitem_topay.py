# Generated by Django 5.0.3 on 2024-04-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0028_alter_itemimage_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='topay',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
