# Generated by Django 4.0.3 on 2024-03-26 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0009_alter_reviewitem_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystore',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
