# Generated by Django 5.0.3 on 2024-04-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0036_alter_storeitem_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]