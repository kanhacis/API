# Generated by Django 5.0.3 on 2024-04-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0037_storeitem_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='open_to_sell',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
