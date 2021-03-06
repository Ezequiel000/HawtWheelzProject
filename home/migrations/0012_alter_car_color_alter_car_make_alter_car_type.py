# Generated by Django 4.0.3 on 2022-05-02 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_car_type_alter_car_color_alter_car_make'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('Green', 'Green'), ('Silver', 'Silver'), ('White', 'White'), ('Blue', 'Blue'), ('Red', 'Red'), ('Black', 'Black')], default='color', max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(choices=[('Kia', 'Kia'), ('Polestar', 'Polestar'), ('FIAT', 'FIAT'), ('Porche', 'Porche'), ('Tesla', 'Tesla'), ('Chevrolet', 'Chevrolet'), ('Audi', 'Audi'), ('Jeep', 'Jeep'), ('GMC', 'GMC'), ('Ford', 'Ford'), ('Hyundai', 'Hyundai')], default='make', max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(choices=[('Pick-up', 'Pick-up'), ('Coupe', 'Coupe'), ('Compact', 'Compact'), ('Sports', 'Sports'), ('Sedan', 'Sedan'), ('SUV', 'SUV')], default='type', max_length=20, null=True),
        ),
    ]
