# Generated by Django 4.2.4 on 2023-09-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemId', models.CharField(max_length=50)),
                ('available', models.BooleanField()),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('price', models.BigIntegerField()),
                ('priceType', models.CharField(max_length=50)),
                ('defaultTaxRates', models.BooleanField()),
                ('stockCount', models.IntegerField()),
                ('modifiedTime', models.BigIntegerField()),
                ('colorCode', models.CharField(max_length=50)),
            ],
        ),
    ]
