# Generated by Django 4.0.2 on 2022-03-28 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_car_date_added_alter_car_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NavBar',
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='color', max_length=20),
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='date_added',
            field=models.DateTimeField(verbose_name='date added'),
        ),
    ]