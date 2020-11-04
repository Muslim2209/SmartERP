# Generated by Django 3.1.2 on 2020-10-04 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document', '0001_initial'),
        ('company', '0003_auto_20201003_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='document.maininfo'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]