# Generated by Django 2.1.7 on 2020-03-19 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_auto_20200319_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='product_date',
            field=models.DateField(help_text='Date format: yyyy-mm-dd', verbose_name='Product Date'),
        ),
    ]
