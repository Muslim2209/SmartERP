from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=960, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    web_site = models.URLField(null=True, blank=True)
    qr_code = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    inn = models.IntegerField(null=True, blank=True)
    city = models.ForeignKey('reference.City', on_delete=models.PROTECT, null=True, blank=True)
    address = models.CharField(max_length=960, null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    latitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Info - {self.name or self.phone_number or self.description or self.email}'


class Document(models.Model):
    image = models.ImageField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}'
