# Generated by Django 3.1.2 on 2020-10-05 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_auto_20201004_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='remain',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]