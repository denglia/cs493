# Generated by Django 2.1.7 on 2020-03-18 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kiosk',
            fields=[
                ('phoneNumber', models.IntegerField(primary_key=True, serialize=False, verbose_name='Phone Number')),
                ('zip', models.IntegerField(verbose_name='Zip')),
                ('stock_quantity', models.IntegerField(verbose_name='Stock Quantity')),
                ('manufacturers', models.ManyToManyField(to='my_app.Manufacturer')),
            ],
        ),
    ]
