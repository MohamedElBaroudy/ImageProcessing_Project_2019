# Generated by Django 2.2 on 2019-05-02 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0003_auto_20190427_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='zones',
            field=models.ManyToManyField(to='bus.Zone'),
        ),
    ]