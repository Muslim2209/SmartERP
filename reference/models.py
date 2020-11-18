from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, related_name='regions')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)
    region = models.ForeignKey('Region', on_delete=models.PROTECT, related_name='cities')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name
