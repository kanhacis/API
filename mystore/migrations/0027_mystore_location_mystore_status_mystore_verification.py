# Generated by Django 4.0.3 on 2024-03-28 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0026_alter_itemimage_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystore',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mystore',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='mystore',
            name='verification',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
