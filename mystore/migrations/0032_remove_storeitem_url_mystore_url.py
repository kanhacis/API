# Generated by Django 5.0.3 on 2024-04-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0031_storeitem_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeitem',
            name='url',
        ),
        migrations.AddField(
            model_name='mystore',
            name='url',
            field=models.ImageField(blank=True, null=True, upload_to='storeImages/'),
        ),
    ]
