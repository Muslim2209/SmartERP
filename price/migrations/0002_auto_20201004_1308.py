# Generated by Django 3.1.2 on 2020-10-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'currencies'},
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]
