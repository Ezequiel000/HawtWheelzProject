# Generated by Django 4.0.3 on 2022-03-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_car_date_added_alter_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='option_text',
            field=models.CharField(max_length=200),
        ),
    ]