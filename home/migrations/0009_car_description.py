# Generated by Django 4.0.2 on 2022-04-01 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_navbar_alter_car_date_added_alter_car_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.CharField(default='des', max_length=500),
        ),
    ]
