# Generated by Django 3.1.2 on 2020-10-07 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0003_city'),
        ('document', '0002_auto_20201005_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maininfo',
            name='region',
        ),
        migrations.AddField(
            model_name='maininfo',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reference.city'),
        ),
    ]