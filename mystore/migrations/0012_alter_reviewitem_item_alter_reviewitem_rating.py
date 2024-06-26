# Generated by Django 4.0.3 on 2024-03-26 14:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0011_storeitem_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_item', to='mystore.storeitem'),
        ),
        migrations.AlterField(
            model_name='reviewitem',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
