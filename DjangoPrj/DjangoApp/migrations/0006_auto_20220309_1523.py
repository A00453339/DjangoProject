# Generated by Django 3.2.12 on 2022-03-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0005_auto_20220309_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='check_in_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='check_out_date',
            field=models.DateField(),
        ),
    ]
