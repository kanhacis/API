# Generated by Django 5.0.3 on 2024-04-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0032_remove_storeitem_url_mystore_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='freeze_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='storeitem',
            name='frozen',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
