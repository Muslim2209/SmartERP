from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Case(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
