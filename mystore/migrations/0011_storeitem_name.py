# Generated by Django 4.0.3 on 2024-03-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0010_mystore_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]