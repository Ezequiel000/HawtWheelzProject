# Generated by Django 4.0.3 on 2022-03-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_car_date_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ('date_added',)},
        ),
        migrations.AlterField(
            model_name='car',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
