# Generated by Django 2.2.5 on 2019-09-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedOrder',
            fields=[
                ('orderId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('orderDate', models.DateTimeField()),
                ('customerId', models.CharField(max_length=255)),
                ('units', models.IntegerField()),
                ('amount', models.FloatField()),
                ('remarks', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=1000)),
            ],
        ),
    ]