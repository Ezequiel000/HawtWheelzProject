# Generated by Django 4.0.2 on 2022-03-31 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220312_2135'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NavBar',
        ),
        migrations.AlterField(
            model_name='car',
            name='date_added',
            field=models.DateTimeField(verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]