# Generated by Django 3.1.2 on 2020-10-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20201005_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]