# Generated by Django 4.0.3 on 2024-03-28 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0021_storeitem_price_storeitem_standard_storeitem_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitem',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storeItem', to='mystore.mystore'),
        ),
    ]