# Generated by Django 4.0.2 on 2022-03-03 17:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_car_product_image_car_date_added_car_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 17, 16, 39, 820493, tzinfo=utc), verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(default='home/images/empty-default.jpg', upload_to='home/images'),
        ),
    ]