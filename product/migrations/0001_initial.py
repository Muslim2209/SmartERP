# Generated by Django 3.1.2 on 2020-10-03 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('document', '0001_initial'),
        ('unit', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('qr_code', models.CharField(max_length=255)),
                ('netto', models.IntegerField(blank=True, null=True)),
                ('brutto', models.IntegerField(blank=True, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('case_amount', models.IntegerField(blank=True, null=True)),
                ('case_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='unit.case')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='category.category')),
                ('document', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='document.document')),
                ('unit_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='unit.unit')),
            ],
        ),
    ]