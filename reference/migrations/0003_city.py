# Generated by Django 3.1.2 on 2020-10-07 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0002_auto_20201003_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='reference.region')),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]