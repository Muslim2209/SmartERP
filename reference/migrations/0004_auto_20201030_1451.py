# Generated by Django 3.1.2 on 2020-10-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0003_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]