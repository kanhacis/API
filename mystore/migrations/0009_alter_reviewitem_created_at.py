# Generated by Django 4.2.7 on 2024-03-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0008_alter_reviewitem_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewitem',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]